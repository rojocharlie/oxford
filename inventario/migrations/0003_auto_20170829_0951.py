# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20170829_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maestro',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
