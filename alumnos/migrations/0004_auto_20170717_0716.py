# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 13:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_auto_20170717_0710'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoSangre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sangre', models.CharField(max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='sangre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.TipoSangre'),
        ),
    ]