# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 19:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0016_auto_20170724_0333'),
    ]

    operations = [
        migrations.CreateModel(
            name='NivelIngles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='datospersonales',
            name='nivel_ingles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alumnos.NivelIngles'),
        ),
    ]
