# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-20 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inga', '0007_auto_20170320_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featuretablerawdata',
            name='Date_Update',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='featuretablerawdata',
            name='MZ',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='featuretablerawdata',
            name='PC_ID',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='featuretablerawdata',
            name='RT',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='featuretablerawdata',
            name='TIC',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='featuretablerawdata',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inga.UPLCResult'),
        ),
        migrations.AlterField(
            model_name='featuretablerawdata',
            name='species_code_sample',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
