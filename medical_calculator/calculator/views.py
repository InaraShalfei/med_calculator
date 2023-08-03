import datetime
import json
from typing import List

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import Examination, NormalParameter
from django.db.models import Q


def get_normatives():
    normatives_dict = {
        'RBC': NormalParameter.objects.get(name='RBC'),
        'HGB': NormalParameter.objects.get(name='HGB'),
        'MCV': NormalParameter.objects.get(name='MCV'),
        'MCH': NormalParameter.objects.get(name='MCH'),
        'МСНС': NormalParameter.objects.get(name='МСНС'),
        'TIBC': NormalParameter.objects.get(name='TIBC'),
        'transferrin': NormalParameter.objects.get(name='transferrin'),
        'ferritin': NormalParameter.objects.get(name='ferritin'),
        'fe': NormalParameter.objects.get(name='fe'),
        'В9': NormalParameter.objects.get(name='В9'),
        'B12': NormalParameter.objects.get(name='B12'),
        'total_bilirubin': NormalParameter.objects.get(name='total_bilirubin'),
        'LDH': NormalParameter.objects.get(name='LDH'),
        'homocystein': NormalParameter.objects.get(name='homocystein')
    }
    return normatives_dict


def is_anemia_1(examination: Examination) -> (bool, List):
    RBC = examination.RBC if examination.RBC else 0
    HGB = examination.HGB if examination.HGB else 0
    MCV = examination.MCV if examination.MCV else 0
    MCH = examination.MCH if examination.MCH else 0
    MCHC = examination.MCHC if examination.MCHC else 0
    ferritin = examination.ferritin if examination.ferritin else 0
    fe = examination.fe if examination.fe else 0

    if (RBC >= 3.80 and
            HGB >= 110 and
            75.5 <= MCV <= 98 and
            MCH >= 25 and
            MCHC >= 300 and
            ferritin <= 21 and
            fe >= 5):
        return True, []
    return False, []


def is_anemia_2(examination: Examination) -> (bool, List):
    RBC = examination.RBC if examination.RBC else 0
    HGB = examination.HGB if examination.HGB else 0
    MCV = examination.MCV if examination.MCV else 0
    MCH = examination.MCH if examination.MCH else 0
    MCHC = examination.MCHC if examination.MCHC else 0
    ferritin = examination.ferritin if examination.ferritin else 0
    fe = examination.fe if examination.fe else 0

    if (RBC <= 5.10 and
            HGB <= 150 and
            70 <= MCV <= 97 and
            20 <= MCH <= 34 and
            280 <= MCHC <= 350 and
            ferritin <= 12.5 and
            fe <= 8.0):
        additional_parameters = ["TIBC", "transferrin"]
        for parameter in additional_parameters:
            if getattr(examination, parameter, None) is None:
                return None, additional_parameters

        if (examination.transferrin >= 2.5 and
                examination.TIBC >= 35.1):
            return True, []
    return False, []


def is_anemia_3(examination: Examination) -> (bool, List):
    RBC = examination.RBC if examination.RBC else 0
    HGB = examination.HGB if examination.HGB else 0
    MCV = examination.MCV if examination.MCV else 0
    MCH = examination.MCH if examination.MCH else 0
    MCHC = examination.MCHC if examination.MCHC else 0
    ferritin = examination.ferritin if examination.ferritin else 0
    fe = examination.fe if examination.fe else 0

    if (RBC < 3.5 and
            HGB <= 90 and
            MCV <= 80 and
            MCH <= 25 and
            MCHC <= 300 and
            ferritin <= 8.0 and
            fe <= 8.0):
        additional_parameters = ["TIBC", "transferrin"]
        for parameter in additional_parameters:
            if getattr(examination, parameter, None) is None:
                return None, additional_parameters

        if (examination.transferrin >= 3.0 and
                examination.TIBC >= 58):
            return True, []
    return False, []


def is_anemia_B9(examination: Examination) -> (bool, List):
    if (examination.HGB <= 100 and
            examination.MCV >= 94):
        additional_parameters = ["B9", "B12", "homocystein"]
        for parameter in additional_parameters:
            if getattr(examination, parameter, None) is None:
                return None, additional_parameters

        if (examination.homocystein > 13 and
                examination.B9 <= 9 and
                examination.B12 <= 600):
            return True, []
    return False, []


def is_anemia_B12(examination: Examination) -> (bool, List):
    if (examination.HGB <= 100 and
            examination.MCV >= 94):
        additional_parameters = ["B9", "B12", "homocystein"]
        for parameter in additional_parameters:
            if getattr(examination, parameter, None) is None:
                return None, additional_parameters

        if (examination.homocystein > 13 and
                examination.B9 >= 9.0 and
                examination.B12 <= 200):
            return True, []
    return False, []


def is_normal_health(examination: Examination) -> (bool, List):
    normatives = get_normatives()
    if (normatives['RBC'].is_normal(examination.RBC) and
            normatives['HGB'].is_normal(examination.HGB) and
            normatives['MCV'].is_normal(examination.MCV) and
            normatives['MCH'].is_normal(examination.MCH) and
            normatives['МСНС'].is_normal(examination.MCHC) and
            normatives['ferritin'].is_normal(examination.ferritin) and
            normatives['fe'].is_normal(examination.fe)):
        return True, []
    return False, []


def get_diagnoses(examination: Examination) -> (List, List):
    diagnoses_callbacks = {
        is_anemia_1: "Железодефицитная анемия",
        is_anemia_2: "Железодефицитная анемия",
        is_anemia_3: 'Железодефицитная анемия',
        is_anemia_B9: 'В9 дефицитная анемия',
        is_anemia_B12: 'В12 дефицитная анемия',
        is_normal_health: 'У вас нет признаков анемии, вы здоровы'
    }

    diagnoses = []
    need_to_ask = []
    for func, diagnosis in diagnoses_callbacks.items():
        result, additional_parameters = func(examination)
        if result:
            diagnoses.append(diagnosis)
        elif len(additional_parameters):
            need_to_ask.extend(additional_parameters)
    return diagnoses, list(set(need_to_ask))

@csrf_exempt
def handle_results(request):
    request_data = json.loads(request.body.decode('utf-8'))
    existing_examination_condition = Q(full_name=request_data['full_name']) & Q(diagnosis_date=datetime.datetime.today())
    if Examination.objects.filter(existing_examination_condition).exists():
        Examination.objects.filter(existing_examination_condition).update(
            RBC=request_data['RBC'] if 'RBC' in request_data else None,
            HGB=request_data['HGB'] if 'HGB' in request_data else None,
            MCV=request_data['MCV'] if 'MCV' in request_data else None,
            MCH=request_data['MCH'] if 'MCH' in request_data else None,
            MCHC=request_data['MCHC'] if 'MCHC' in request_data else None,
            ferritin=request_data['ferritin'] if 'ferritin' in request_data else None,
            transferrin=request_data['transferrin'] if 'transferrin' in request_data else None,
            TIBC=request_data['TIBC'] if 'TIBC' in request_data else None,
            fe=request_data['fe'] if 'fe' in request_data else None,
            B9=request_data['B9'] if 'B9' in request_data else None,
            B12=request_data['B12'] if 'B12' in request_data else None,
            total_bilirubin=request_data['total_bilirubin'] if 'total_bilirubin' in request_data else None,
            LDH=request_data['LDH'] if 'LDH' in request_data else None,
            homocystein=request_data['homocystein'] if 'homocystein' in request_data else None,
            direct_antiglobulin_test=request_data[
                'direct_antiglobulin_test'] if 'direct_antiglobulin_test' in request_data else None
        )
        examination = Examination.objects.filter(existing_examination_condition).get()
    else:
        examination = Examination.objects.create(
            full_name=request_data['full_name'],
            RBC=request_data['RBC'] if 'RBC' in request_data else None,
            HGB=request_data['HGB'] if 'HGB' in request_data else None,
            MCV=request_data['MCV'] if 'MCV' in request_data else None,
            MCH=request_data['MCH'] if 'MCH' in request_data else None,
            MCHC=request_data['MCHC'] if 'MCHC' in request_data else None,
            ferritin=request_data['ferritin'] if 'ferritin' in request_data else None,
            transferrin=request_data['transferrin'] if 'transferrin' in request_data else None,
            TIBC=request_data['TIBC'] if 'TIBC' in request_data else None,
            fe=request_data['fe'] if 'fe' in request_data else None,
            B9=request_data['B9'] if 'B9' in request_data else None,
            B12=request_data['B12'] if 'B12' in request_data else None,
            total_bilirubin=request_data['total_bilirubin'] if 'total_bilirubin' in request_data else None,
            LDH=request_data['LDH'] if 'LDH' in request_data else None,
            homocystein=request_data['homocystein'] if 'homocystein' in request_data else None,
            direct_antiglobulin_test=request_data[
                'direct_antiglobulin_test'] if 'direct_antiglobulin_test' in request_data else None
        )

    diagnosis, need_to_ask = get_diagnoses(examination)
    if diagnosis:
        examination.diagnosis = ', '.join(diagnosis)
    elif not len(need_to_ask):
        examination.diagnosis = 'Невозможно диагностировать ваш случай. Рекомендуем обратиться к гематологу'
    else:
        examination.diagnosis = ''
    examination.save()

    return JsonResponse({
        "diagnoses": examination.diagnosis,
        "additional_parameters": [value for value in need_to_ask if getattr(examination, value, None) is None]
    })
