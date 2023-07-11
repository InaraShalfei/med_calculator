from django.db import models


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


class Examination(models.Model):
    full_name = models.CharField(max_length=250, verbose_name='ФИО пациента')
    diagnosis = models.CharField(max_length=250, blank=True, null=True, verbose_name='диагноз')
    diagnosis_date = models.DateField(auto_now=True, verbose_name='дата диагноза')
    RBC = models.FloatField(verbose_name='уровень эритроцитов')
    HGB = models.FloatField(verbose_name='уровень гемоглобина')
    HCT = models.FloatField(verbose_name='гематокрит')
    MCV = models.FloatField(verbose_name='средн. объем эритроцита')
    MCH = models.FloatField(verbose_name='средн. эритроцитарный гемоглобин')
    MCHC = models.FloatField(verbose_name='средн. концентрация гемоглобина в эритроците')
    RDW_CV = models.FloatField(verbose_name='распределение эритроцитов по объёму, КВ')
    RDW_SD = models.FloatField(verbose_name='распределение эритроцитов по объёму, СКВ')
    ferritin = models.FloatField(verbose_name='ферритин')
    transferrin = models.FloatField(verbose_name='трансферрин')
    TIBC = models.FloatField(verbose_name='TIBC')
    fe = models.FloatField(verbose_name='железо')
    B9 = models.FloatField(verbose_name='витамин B9')
    B12 = models.FloatField(verbose_name='витамин B12')
    total_bilirubin = models.FloatField(verbose_name='общий билирубин')
    LDH = models.FloatField(verbose_name='ЛДГ')

    class Meta:
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'

    def __str__(self):
        return self.full_name
