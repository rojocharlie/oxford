# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-31 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20170829_1106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vale',
            options={'ordering': ('no_folio',)},
        ),
        migrations.AlterField(
            model_name='material',
            name='cantidad',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
