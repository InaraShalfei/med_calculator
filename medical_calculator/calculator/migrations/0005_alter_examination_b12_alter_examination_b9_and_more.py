# Generated by Django 4.2.3 on 2023-07-11 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_alter_examination_b12_alter_examination_b9_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='B12',
            field=models.FloatField(blank=True, null=True, verbose_name='витамин B12'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='B9',
            field=models.FloatField(blank=True, null=True, verbose_name='витамин B9'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='HCT',
            field=models.FloatField(blank=True, null=True, verbose_name='гематокрит'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='HGB',
            field=models.FloatField(blank=True, null=True, verbose_name='уровень гемоглобина'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='LDH',
            field=models.FloatField(blank=True, null=True, verbose_name='ЛДГ'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='MCH',
            field=models.FloatField(blank=True, null=True, verbose_name='средн. эритроцитарный гемоглобин'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='MCHC',
            field=models.FloatField(blank=True, null=True, verbose_name='средн. концентрация гемоглобина в эритроците'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='MCV',
            field=models.FloatField(blank=True, null=True, verbose_name='средн. объем эритроцита'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='RBC',
            field=models.FloatField(blank=True, null=True, verbose_name='уровень эритроцитов'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='RDW_CV',
            field=models.FloatField(blank=True, null=True, verbose_name='распределение эритроцитов по объёму, КВ'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='RDW_SD',
            field=models.FloatField(blank=True, null=True, verbose_name='распределение эритроцитов по объёму, СКВ'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='TIBC',
            field=models.FloatField(blank=True, null=True, verbose_name='TIBC'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='fe',
            field=models.FloatField(blank=True, null=True, verbose_name='железо'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='ferritin',
            field=models.FloatField(blank=True, null=True, verbose_name='ферритин'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='total_bilirubin',
            field=models.FloatField(blank=True, null=True, verbose_name='общий билирубин'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='transferrin',
            field=models.FloatField(blank=True, null=True, verbose_name='трансферрин'),
        ),
    ]