# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-01 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0028_remove_perro_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='foto',
            field=models.ImageField(blank=True, upload_to='settings.MEDIA_ROOT'),
        ),
    ]
