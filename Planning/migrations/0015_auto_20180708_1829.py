# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-08 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planning', '0014_auto_20180708_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changebalance',
            name='change',
            field=models.CharField(choices=[('Расход', 'Расход'), ('Поступление', 'Поступление')], default='Расход', max_length=12),
        ),
    ]