# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-04 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_auto_20170831_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='material',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='detallematerial',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Material'),
        ),
    ]