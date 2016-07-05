# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inga', '0002_auto_20160702_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extractionweight',
            name='extraction',
        ),
        migrations.AddField(
            model_name='extraction',
            name='dry_marc_weight',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='extraction',
            name='dry_weight',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='extraction',
            name='empty_vial_weight',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='extraction',
            name='final_weight',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='extraction',
            name='mass_extracted',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='extraction',
            name='percent_extracted',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='extraction',
            name='proportion_remaining',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='ExtractionWeight',
        ),
    ]
