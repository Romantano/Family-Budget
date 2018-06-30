# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-30 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planning', '0003_changebalance'),
    ]

    operations = [
        migrations.AddField(
            model_name='changebalance',
            name='change',
            field=models.CharField(choices=[('Spending', 'Расход'), ('Income', 'Поступление')], default='Расход', max_length=1),
        ),
    ]