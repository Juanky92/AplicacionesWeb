# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-16 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0026_auto_20171106_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='foto',
            field=models.ImageField(blank=True, upload_to='imagen/'),
        ),
    ]
