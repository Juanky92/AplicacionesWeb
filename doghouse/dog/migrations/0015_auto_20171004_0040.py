# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-04 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0014_auto_20171002_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitude',
            name='email',
        ),
        migrations.AddField(
            model_name='perro',
            name='estado',
            field=models.CharField(choices=[('A', 'adoptable'), ('AD', 'adoptado')], default='A', max_length=2),
        ),
        migrations.DeleteModel(
            name='Solicitude',
        ),
    ]
