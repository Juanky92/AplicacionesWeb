# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-06 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0025_auto_20171106_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='estado',
            field=models.CharField(choices=[('A', 'adoptable'), ('AD', 'adoptado')], default='A', max_length=2),
        ),
    ]
