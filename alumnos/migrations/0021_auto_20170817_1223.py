# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0020_datospersonales_correo_escuela'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datospersonales',
            name='correo_escuela',
            field=models.EmailField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]