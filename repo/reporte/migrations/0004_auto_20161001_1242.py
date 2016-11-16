# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-01 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporte', '0003_auto_20160919_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='v_ReporteSecciones',
            fields=[
                ('id', models.CharField(db_column='ID', primary_key=True, serialize=False)),
                ('ubigeo', models.CharField(db_column='UBIGEO', db_index=True, max_length=6)),
                ('zona', models.CharField(db_column='ZONA', max_length=5)),
                ('seccion', models.IntegerField(db_column='SECCION')),
                ('aeu_final', models.IntegerField(db_column='AEU_FINAL')),
                ('manzanas', models.CharField(db_column='MANZANAS', max_length=6)),
                ('cant_viv', models.IntegerField(db_column='CANT_VIV')),
            ],
            options={
                'db_table': 'VW_REPORTE_SECCIONES',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Via',
            fields=[
                ('p20', models.CharField(db_column='P20', db_index=True, max_length=254, primary_key=True, serialize=False)),
                ('p20_nombre', models.CharField(db_column='P20_NOMBRE', max_length=254)),
            ],
            options={
                'db_table': 'TB_TIPO_VIA',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='aeus',
            table='TB_AEUS',
        ),
    ]