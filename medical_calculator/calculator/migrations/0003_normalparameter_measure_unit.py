# Generated by Django 4.2.3 on 2023-07-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_examination_remove_analysisresult_analysis_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='normalparameter',
            name='measure_unit',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='ед. изм-я'),
        ),
    ]