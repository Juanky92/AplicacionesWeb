# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-01 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0029_perro_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='foto',
            field=models.ImageField(upload_to='dog/stacti/pic'),
        ),
    ]
