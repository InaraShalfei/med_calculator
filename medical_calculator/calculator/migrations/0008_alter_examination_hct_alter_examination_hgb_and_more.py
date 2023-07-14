# Generated by Django 4.2.3 on 2023-07-14 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0007_examination_direct_antiglobulin_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='HCT',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examination',
            name='HGB',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examination',
            name='MCH',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examination',
            name='MCHC',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examination',
            name='MCV',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examination',
            name='RBC',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examination',
            name='RDW_CV',
            field=models.FloatField(blank=True, null=True, verbose_name='RDW-CV'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='RDW_SD',
            field=models.FloatField(blank=True, null=True, verbose_name='RDW-SD'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='direct_antiglobulin_test',
            field=models.CharField(blank=True, choices=[('POS', 'Положительная'), ('NEG', 'Отрицательная')], max_length=3, null=True, verbose_name='прямая реакция  Кумбса'),
        ),
    ]