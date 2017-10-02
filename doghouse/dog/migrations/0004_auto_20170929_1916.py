# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-29 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0003_auto_20170929_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='raza',
            name='Cruze',
        ),
        migrations.RemoveField(
            model_name='raza',
            name='Descripcion',
        ),
        migrations.AddField(
            model_name='perro',
            name='Cruze',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perro',
            name='Descripcion',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
