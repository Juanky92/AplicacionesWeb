# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-04 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0016_auto_20171004_0049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perro',
            old_name='micropchip',
            new_name='microchip',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cp',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='edad',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=15),
        ),
    ]
