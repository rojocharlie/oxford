# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0007_auto_20170719_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datospersonales',
            name='sangre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alumnos.TipoSangre'),
        ),
    ]
