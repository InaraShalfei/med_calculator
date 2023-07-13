import datetime
import json
from typing import List

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .models import Examination, NormalParameter
from django.db.models import Q


def get_normatives():
    normatives_dict = {
        'RBC': NormalParameter.objects.get(name='RBC'),
        'HGB': NormalParameter.objects.get(name='HGB'),
        'HCT': NormalParameter.objects.get(name='HCT'),
        'MCV': NormalParameter.objects.get(name='MCV'),
        'MCH': NormalParameter.objects.get(name='MCH'),
        'МСНС': NormalParameter.objects.get(name='МСНС'),
        'RDW_CV': NormalParameter.objects.get(name='RDW_CV'),
        'RDW_SD': NormalParameter.objects.get(name='RDW_SD'),
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


def is_anemia_1(examination: Examination) -> bool:
    normatives = get_normatives()
    if (normatives['RBC'].is_normal_or_high(examination.RBC) and
            normatives['HGB'].is_normal(examination.HGB) and
            normatives['HCT'].is_normal(examination.HCT) and
            normatives['MCV'].is_normal(examination.MCV) and
            normatives['MCH'].is_normal(examination.MCH) and
            normatives['МСНС'].is_normal(examination.MCHC) and
            normatives['RDW_CV'].is_normal(examination.RDW_CV) and
            normatives['RDW_SD'].is_normal(examination.RDW_SD) and
            normatives['TIBC'].is_normal(examination.TIBC) and
            normatives['transferrin'].is_normal(examination.transferrin) and
            normatives['ferritin'].is_equal_to_low_or_lower(examination.ferritin) and
            normatives['fe'].is_low(examination.fe)):
        return True


def is_anemia_2(examination: Examination) -> bool:
    normatives = get_normatives()
    if (normatives['RBC'].is_normal_or_low(examination.RBC) and
            normatives['HGB'].is_low(examination.HGB) and
            normatives['HCT'].is_equal_to_low_or_lower(examination.HCT) and
            normatives['MCV'].is_equal_to_low_or_lower(examination.MCV) and
            normatives['MCH'].is_equal_to_low_or_lower(examination.MCH) and
            normatives['МСНС'].is_equal_to_low_or_lower(examination.MCHC) and
            normatives['RDW_CV'].is_normal_or_high(examination.RDW_CV) and
            normatives['RDW_SD'].is_normal(examination.RDW_SD) and
            normatives['ferritin'].is_equal_to_low_or_lower(examination.ferritin) and
            normatives['fe'].is_low(examination.fe) and
            normatives['transferrin'].is_normal_or_high(examination.transferrin) and
            normatives['TIBC'].is_high(examination.TIBC) and
            normatives['В9'].is_normal(examination.B9) and
            normatives['B12'].is_normal(examination.B12)):
        return True


def is_anemia_3(examination: Examination) -> bool:
    normatives = get_normatives()
    if (normatives['RBC'].is_low(examination.RBC) and
            normatives['HGB'].is_low(examination.HGB) and
            normatives['HCT'].is_low(examination.HCT) and
            normatives['MCV'].is_low(examination.MCV) and
            normatives['MCH'].is_low(examination.MCH) and
            normatives['МСНС'].is_equal_to_low_or_lower(examination.MCHC) and
            normatives['RDW_CV'].is_normal_or_high(examination.RDW_CV) and
            normatives['RDW_SD'].is_normal_or_high(examination.RDW_SD) and
            normatives['ferritin'].is_low(examination.ferritin) and
            normatives['fe'].is_low(examination.fe) and
            normatives['transferrin'].is_normal_or_high(examination.transferrin) and
            normatives['TIBC'].is_high(examination.TIBC) and
            normatives['total_bilirubin'].is_normal_or_high(examination.total_bilirubin) and
            normatives['В9'].is_equal_to_low_or_lower(examination.B9) and
            normatives['B12'].is_equal_to_low_or_lower(examination.B12)):
        return True


def is_anemia_B9(examination: Examination) -> bool:
    normatives = get_normatives()
    if (normatives['RBC'].is_equal_to_low_or_lower(examination.RBC) and
            normatives['HGB'].is_low(examination.HGB) and
            normatives['MCV'].is_normal_or_high(examination.MCV) and #check
            normatives['MCH'].is_normal_or_low(examination.MCH) and
            normatives['МСНС'].is_normal_or_low(examination.MCHC) and
            normatives['ferritin'].is_low(examination.ferritin) and
            normatives['fe'].is_low(examination.fe) and
            normatives['transferrin'].is_normal_or_high(examination.transferrin) and
            normatives['LDH'].is_normal_or_high(examination.LDH) and
            normatives['total_bilirubin'].is_normal_or_high(examination.total_bilirubin) and
            normatives['TIBC'].is_normal_or_low(examination.TIBC) and
            normatives['homocystein'].is_high(examination.homocystein) and
            examination.B9 <= 8.0 and
            normatives['B12'].is_normal(examination.B12)):
        return True


def is_anemia_B12(examination: Examination) -> bool:
    normatives = get_normatives()
    if (normatives['RBC'].is_equal_to_low_or_lower(examination.RBC) and
            normatives['HGB'].is_low(examination.HGB) and
            normatives['MCV'].is_normal_or_high(examination.MCV) and
            normatives['MCH'].is_normal_or_low(examination.MCH) and
            normatives['МСНС'].is_normal_or_low(examination.MCHC) and
            normatives['ferritin'].is_low(examination.ferritin) and
            normatives['fe'].is_low(examination.fe) and
            normatives['transferrin'].is_normal_or_low(examination.transferrin) and
            normatives['total_bilirubin'].is_normal(examination.total_bilirubin) and
            normatives['LDH'].is_high(examination.LDH) and
            normatives['TIBC'].is_equal_to_low_or_lower(examination.TIBC) and
            normatives['homocystein'].is_high(examination.homocystein) and
            normatives['В9'].is_normal(examination.B9) and
            normatives['B12'].is_low(examination.B12)):
        return True


def is_autoimmune_anemia(examination: Examination) -> bool:
    normatives = get_normatives()
    if (normatives['RBC'].is_low(examination.RBC) and
            normatives['HGB'].is_low(examination.HGB) and
            normatives['HCT'].is_equal_to_low_or_lower(examination.HCT) and
            normatives['MCV'].is_normal_or_high(examination.MCV) and
            normatives['MCH'].is_normal_or_low(examination.MCH) and
            normatives['МСНС'].is_normal_or_high(examination.MCHC) and
            normatives['ferritin'].is_normal_or_high(examination.ferritin) and
            normatives['fe'].is_normal_or_high(examination.fe) and
            normatives['transferrin'].is_normal_or_high(examination.transferrin) and
            normatives['TIBC'].is_high(examination.TIBC) and
            normatives['total_bilirubin'].is_high(examination.total_bilirubin) and
            normatives['LDH'].is_high(examination.LDH) and
            examination.direct_antiglobulin_test == 'Положительная'):
        return True

def is_normal_health(examination:Examination) -> bool:
    normatives = get_normatives()
    if (normatives['RBC'].is_normal(examination.RBC) and
            normatives['HGB'].is_normal(examination.HGB) and
            normatives['HCT'].is_normal(examination.HCT) and
            normatives['MCV'].is_normal(examination.MCV) and
            normatives['MCH'].is_normal(examination.MCH) and
            normatives['МСНС'].is_normal(examination.MCHC) and
            normatives['RDW_SD'].is_normal(examination.RDW_SD) and
            normatives['RDW_CV'].is_normal(examination.RDW_CV) and
            normatives['ferritin'].is_normal(examination.ferritin) and
            normatives['fe'].is_normal(examination.fe) and
            normatives['transferrin'].is_normal(examination.transferrin) and
            normatives['В9'].is_normal(examination.B9) and
            normatives['В12'].is_normal(examination.B12) and
            normatives['TIBC'].is_normal(examination.TIBC) and
            normatives['total_bilirubin'].is_normal(examination.total_bilirubin) and
            normatives['LDH'].is_normal(examination.LDH) and
            normatives['homocystein'].is_normal(examination.homocystein) and
            examination.direct_antiglobulin_test == 'Отрицательная'):
        return True


def get_diagnoses(examination:Examination) -> List:
    diagnoses_callbacks = {
        is_anemia_1: '1 степень железодефицитной анемии',
        is_anemia_2: '2 степень железодефицитной анемии',
        is_anemia_3: '3 степень железодефицитной анемии',
        is_anemia_B9: 'В9 дефицитная анемия',
        is_anemia_B12: 'В12 дефицитная анемия',
        is_autoimmune_anemia: 'Аутоиммунная гемолитическая анемия',
        is_normal_health: 'У вас нет признаков анемии, вы здоровы'
    }

    diagnoses = []
    for func, diagnosis in diagnoses_callbacks.items():
        if func(examination):
            diagnoses.append(diagnosis)
    return diagnoses

@csrf_exempt
def handle_results(request):
    request_data = json.loads(request.body.decode('utf-8'))
    existing_examination_condition = Q(full_name=request_data['full_name']) & Q(diagnosis_date=datetime.datetime.today())
    if Examination.objects.filter(existing_examination_condition).exists():
        Examination.objects.filter(existing_examination_condition).update(
            RBC=request_data['RBC'] if 'RBC' in request_data else None,
            HGB=request_data['HGB'] if 'HGB' in request_data else None,
            HCT=request_data['HCT'] if 'HCT' in request_data else None,
            MCV=request_data['MCV'] if 'MCV' in request_data else None,
            MCH=request_data['MCH'] if 'MCH' in request_data else None,
            MCHC=request_data['MCHC'] if 'MCHC' in request_data else None,
            RDW_CV=request_data['RDW_CV'] if 'RDW_CV' in request_data else None,
            RDW_SD=request_data['RDW_SD'] if 'RDW_SD' in request_data else None,
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
            HCT=request_data['HCT'] if 'HCT' in request_data else None,
            MCV=request_data['MCV'] if 'MCV' in request_data else None,
            MCH=request_data['MCH'] if 'MCH' in request_data else None,
            MCHC=request_data['MCHC'] if 'MCHC' in request_data else None,
            RDW_CV=request_data['RDW_CV'] if 'RDW_CV' in request_data else None,
            RDW_SD=request_data['RDW_SD'] if 'RDW_SD' in request_data else None,
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

    diagnosis = get_diagnoses(examination)
    examination.diagnosis = ', '.join(diagnosis)
    examination.save()


    return HttpResponse(examination.diagnosis)




