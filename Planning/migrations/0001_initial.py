# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-30 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(default=0, max_length=10, verbose_name='Текущий баланс')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название:')),
                ('start_Date', models.DateField(verbose_name='Укажите начало периода:')),
                ('end_Date', models.DateField(verbose_name='Укажите конец периода:')),
            ],
        ),
    ]