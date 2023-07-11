from django.db import models


class NormalParameter(models.Model):
    name = models.CharField(max_length=250, verbose_name='показатель')
    low_limit = models.IntegerField(verbose_name='нижний предел нормы')
    high_limit = models.IntegerField(verbose_name='верхний предел нормы')

    class Meta:
        verbose_name = 'Показатель нормы'
        verbose_name_plural = 'Показатели нормы'

    def __str__(self):
        return self.name


class Patient(models.Model):
    full_name = models.CharField(max_length=250, verbose_name='ФИО пациента')

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    def __str__(self):
        return self.full_name


class Analysis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='пациент', related_name='analyses')
    date_of_analysis = models.DateField(verbose_name='дата анализа')

    class Meta:
        verbose_name = 'Анализ'
        verbose_name_plural = 'Анализы'


class AnalysisResult(models.Model):
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE, verbose_name='анализ', related_name='results')
    parameter = models.ForeignKey(NormalParameter, on_delete=models.CASCADE, verbose_name='параметр', related_name='results')
    result = models.IntegerField(verbose_name='результат')

    class Meta:
        verbose_name = 'Показатель анализа'
        verbose_name_plural = 'Показатели анализа'


class Diagnosis(models.Model):
    name = models.CharField(max_length=250, verbose_name='диагноз')


class DiagnosisByAnalysis(models.Model):
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE, verbose_name='анализ', related_name='diagnoses')
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE, verbose_name='диагноз', related_name='diagnoses')
