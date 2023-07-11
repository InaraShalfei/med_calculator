import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .models import Examination


@csrf_exempt
def handle_results(request):
    request_data = json.loads(request.body.decode('utf-8'))
    patient, created = Examination.objects.get_or_create(full_name=request_data['full_name'], RBC=request_data['RBC'],
                                                         HGB=request_data['HGB'], HCT=request_data['HCT'],
                                                         MCV=request_data['MCV'], MCH=request_data['MCH'],
                                                         MCHC=request_data['MCHC'], RDW_CV=request_data['RDW_CV'],
                                                         RDW_SD=request_data['RDW_SD'], ferritin=request_data['ferritin'],
                                                         transferrin=request_data['transferrin'], TIBC=request_data['TIBC'],
                                                         fe=request_data['fe'], B9=request_data['B9'], B12=request_data['B12'],
                                                         total_bilirubin=request_data['total_bilirubin'],
                                                         LDH=request_data['LDH'])
    print(json.loads(request.body.decode('utf-8'))['full_name'])

    return HttpResponse()




