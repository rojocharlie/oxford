# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_auto_20170809_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='link_galeria',
            field=models.URLField(blank=True, max_length=250, null=True),
        ),
    ]
