import datetime

from django.db import models
from django.contrib import admin


class NormalParameter(models.Model):
    name = models.CharField(max_length=250, verbose_name='название показателя')
    title = models.CharField(blank=True, null=True, max_length=250, verbose_name='описание показателя')
    low_limit = models.FloatField(verbose_name='нижний предел нормы')
    high_limit = models.FloatField(verbose_name='верхний предел нормы')
    measure_unit = models.CharField(max_length=10, blank=True, null=True, verbose_name='ед. изм-я')

    class Meta:
        verbose_name = 'Показатель нормы'
        verbose_name_plural = 'Показатели нормы'

    def __str__(self):
        return self.name

    def is_normal(self, value):
        return self.low_limit <= value <= self.high_limit

    def is_normal_or_high(self, value):
        return value >= self.low_limit

    def is_normal_or_low(self, value):
        return value <= self.low_limit

    def is_low(self, value):
        return value < self.low_limit

    def is_high(self, value):
        return value > self.high_limit


class Examination(models.Model):
    full_name = models.CharField(max_length=250, verbose_name='ФИО пациента')
    diagnosis = models.CharField(max_length=250, blank=True, null=True, verbose_name='диагноз')
    diagnosis_date = models.DateField(auto_now=True, verbose_name='дата диагноза')
    RBC = models.FloatField(verbose_name='уровень эритроцитов', blank=True, null=True)
    HGB = models.FloatField(verbose_name='уровень гемоглобина', blank=True, null=True)
    HCT = models.FloatField(verbose_name='гематокрит', blank=True, null=True)
    MCV = models.FloatField(verbose_name='средн. объем эритроцита', blank=True, null=True)
    MCH = models.FloatField(verbose_name='средн. эритроцитарный гемоглобин', blank=True, null=True)
    MCHC = models.FloatField(verbose_name='средн. концентрация гемоглобина в эритроците', blank=True, null=True)
    RDW_CV = models.FloatField(verbose_name='распределение эритроцитов по объёму, КВ', blank=True, null=True)
    RDW_SD = models.FloatField(verbose_name='распределение эритроцитов по объёму, СКВ', blank=True, null=True)
    ferritin = models.FloatField(verbose_name='ферритин', blank=True, null=True)
    transferrin = models.FloatField(verbose_name='трансферрин', blank=True, null=True)
    TIBC = models.FloatField(verbose_name='TIBC', blank=True, null=True)
    fe = models.FloatField(verbose_name='железо', blank=True, null=True)
    B9 = models.FloatField(verbose_name='витамин B9', blank=True, null=True)
    B12 = models.FloatField(verbose_name='витамин B12', blank=True, null=True)
    total_bilirubin = models.FloatField(verbose_name='общий билирубин', blank=True, null=True)
    LDH = models.FloatField(verbose_name='ЛДГ', blank=True, null=True)
    homocystein = models.FloatField(verbose_name=' гомоцистеин', blank=True, null=True)

    class Meta:
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'

    def __str__(self):
        return self.full_name

    @admin.display(description='Дата диагноза')
    def readable_date(self):
        date = datetime.datetime.strptime(str(self.diagnosis_date), '%Y-%m-%d')
        return datetime.datetime.strftime(date, '%d.%m.%Y')

