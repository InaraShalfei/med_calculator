from django.contrib import admin

from .models import NormalParameter, Examination


class NormalParameterAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'measure_unit', 'low_limit', 'high_limit')
    empty_value_display = '-пусто-'


class ExaminationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'diagnosis', 'readable_date', 'RBC', 'HGB', 'HCT', 'MCV', 'MCH', 'MCHC', 'RDW_CV', 'RDW_SD',
                    'ferritin', 'transferrin', 'TIBC', 'fe', 'B9', 'B12', 'total_bilirubin', 'LDH')
    empty_value_display = '-пусто-'


admin.site.register(NormalParameter, NormalParameterAdmin)
admin.site.register(Examination, ExaminationAdmin)
