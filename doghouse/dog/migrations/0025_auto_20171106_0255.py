# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-06 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0024_auto_20171026_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='estado',
            field=models.CharField(choices=[('Adoptable', 'adoptable'), ('Adoptado', 'adoptado')], default='Adoptable', max_length=2),
        ),
    ]
