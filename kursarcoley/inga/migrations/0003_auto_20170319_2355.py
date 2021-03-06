# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 23:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inga', '0002_auto_20170319_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='field',
            name='herbivores_present',
        ),
        migrations.AlterField(
            model_name='field',
            name='ant_collection_number',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='ants',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='ants_efn',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='efn',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='exp_max',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='exp_min',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='exp_vs_mat',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='original_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='plant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inga.Plant'),
        ),
    ]
