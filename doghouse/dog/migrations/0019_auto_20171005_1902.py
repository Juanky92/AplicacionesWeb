# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-05 19:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0018_auto_20171004_1921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raza',
            old_name='Raza',
            new_name='raza',
        ),
    ]
