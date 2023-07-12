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
        'В12': NormalParameter.objects.get(name='В12')
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
            normatives['ferritin'].is_normal_or_low(examination.ferritin) and
            normatives['fe'].is_low(examination.fe)):
        return True


def is_anemia_2(examination: Examination) -> bool:
    normatives = get_normatives()
    if (normatives['RBC'].is_normal_or_low(examination.RBC) and
            normatives['HGB'].is_low(examination.HGB) and
            normatives['HCT'].is_normal_or_low(examination.HCT) and
            normatives['MCV'].is_normal_or_low(examination.MCV) and
            normatives['MCH'].is_normal_or_low(examination.MCH) and
            normatives['МСНС'].is_normal_or_low(examination.MCHC) and
            normatives['RDW_CV'].is_normal_or_high(examination.RDW_CV) and
            normatives['RDW_SD'].is_normal(examination.RDW_SD) and
            normatives['ferritin'].is_normal_or_low(examination.ferritin) and
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
            normatives['МСНС'].is_normal_or_low(examination.MCHC) and
            normatives['RDW_CV'].is_normal_or_high(examination.RDW_CV) and
            normatives['RDW_SD'].is_normal_or_high(examination.RDW_SD) and
            normatives['ferritin'].is_low(examination.ferritin) and
            normatives['fe'].is_low(examination.fe) and
            normatives['transferrin'].is_normal_or_high(examination.transferrin) and
            normatives['TIBC'].is_high(examination.TIBC) and
            normatives['total_bilirubin'].is_normal_or_high(examination.total_bilirubin) and
            normatives['В9'].is_normal(examination.B9) and
            normatives['B12'].is_normal(examination.B12)):
        return True


def get_diagnosises(examination:Examination) -> List:
    diagnoses_callbacks = {
        is_anemia_1: '1 степень железодефицитной анемии',
        is_anemia_2: '2 степень железодефицитной анемии',
        is_anemia_3: '3 степень железодефицитной анемии'
    }

    diagnoses = []
    for func, diagnosys in diagnoses_callbacks.items():
        if func(examination):
            diagnoses.append(diagnosys)
    return diagnoses

@csrf_exempt
def handle_results(request):
    request_data = json.loads(request.body.decode('utf-8'))
    if Examination.objects.filter(
            Q(full_name=request_data['full_name']) & Q(diagnosis_date=datetime.datetime.today())).exists():
        examination = Examination.objects.filter(Q(full_name=request_data['full_name']) &
                                   Q(diagnosis_date=datetime.datetime.today())).update(RBC=request_data['RBC'],
                                                                                       HGB=request_data['HGB'],
                                                                                       HCT=request_data['HCT'],
                                                                                       MCV=request_data['MCV'],
                                                                                       MCH=request_data['MCH'],
                                                                                       MCHC=request_data['MCHC'],
                                                                                       RDW_CV=request_data['RDW_CV'],
                                                                                       RDW_SD=request_data['RDW_SD'],
                                                                                       ferritin=request_data[
                                                                                           'ferritin'],
                                                                                       transferrin=request_data[
                                                                                           'transferrin'],
                                                                                       TIBC=request_data['TIBC'],
                                                                                       fe=request_data['fe'],
                                                                                       B9=request_data['B9'],
                                                                                       B12=request_data['B12'],
                                                                                       total_bilirubin=request_data[
                                                                                           'total_bilirubin'],
                                                                                       LDH=request_data['LDH'])
    else:
        examination = Examination.objects.create(full_name=request_data['full_name'], RBC=request_data['RBC'],
                                   HGB=request_data['HGB'], HCT=request_data['HCT'],
                                   MCV=request_data['MCV'], MCH=request_data['MCH'],
                                   MCHC=request_data['MCHC'], RDW_CV=request_data['RDW_CV'],
                                   RDW_SD=request_data['RDW_SD'], ferritin=request_data['ferritin'],
                                   transferrin=request_data['transferrin'], TIBC=request_data['TIBC'],
                                   fe=request_data['fe'], B9=request_data['B9'], B12=request_data['B12'],
                                   total_bilirubin=request_data['total_bilirubin'],
                                   LDH=request_data['LDH'])



    return HttpResponse()




