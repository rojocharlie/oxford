# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('imagen_encabezado', models.ImageField(upload_to='noticias')),
                ('texto_principal', models.TextField()),
                ('imagen_secundaria', models.ImageField(blank=True, null=True, upload_to='noticias')),
                ('texto_secundario', models.TextField(blank=True, null=True)),
                ('imagen_terciaria', models.ImageField(blank=True, null=True, upload_to='noticias')),
                ('texto_terciaria', models.TextField(blank=True, null=True)),
                ('fecha_publicacion', models.DateField(auto_now_add=True)),
                ('fecha_modificacion', models.DateField(auto_now=True)),
                ('link_galeria', models.URLField(max_length=250)),
                ('autor', models.CharField(max_length=50)),
            ],
        ),
    ]
