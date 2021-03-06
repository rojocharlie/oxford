# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0014_auto_20170721_0549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candado', models.IntegerField(default=0)),
                ('papel_china', models.IntegerField(default=0)),
                ('papel_crepe', models.IntegerField(default=0)),
                ('rotafolio_blanco', models.IntegerField(default=0)),
                ('rotafolio_cuadrado', models.IntegerField(default=0)),
                ('papelbond_colores', models.IntegerField(default=0)),
                ('paquete_500hojas_blanca', models.IntegerField(default=0)),
                ('papelestrasa_metro', models.IntegerField(default=0)),
                ('caja_conos', models.IntegerField(default=0)),
                ('paquete_papelsanitario', models.IntegerField(default=0)),
                ('paquete_toallasdepapel', models.IntegerField(default=0)),
                ('caja_pañuelos', models.IntegerField(default=0)),
                ('alumno_inv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.DatosPersonales')),
            ],
        ),
    ]
