# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 17:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='date_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evento',
            name='titulo',
            field=models.CharField(max_length=30),
        ),
    ]
