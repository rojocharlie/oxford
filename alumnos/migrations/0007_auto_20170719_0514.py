# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0006_auto_20170719_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='datospersonales',
            name='apellido',
            field=models.CharField(default='Apellido', max_length=30),
        ),
        migrations.AlterField(
            model_name='escolaridad',
            name='escolaridad',
            field=models.CharField(max_length=10),
        ),
    ]
