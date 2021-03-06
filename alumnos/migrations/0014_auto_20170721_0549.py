# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0013_auto_20170721_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='datospersonales',
            name='correo',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='datospersonales',
            name='correomadre',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='datospersonales',
            name='correopadre',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='alergias',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='enfermedadcronica',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='nombreautorizada',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='nombremadre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='nombrepadre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='ocupacionaut',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='trabajoaut',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='trabajopadre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
