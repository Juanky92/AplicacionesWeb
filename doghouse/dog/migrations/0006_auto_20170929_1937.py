# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-29 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0005_auto_20170929_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Sexo',
            field=models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], default='H', max_length=2),
        ),
    ]
