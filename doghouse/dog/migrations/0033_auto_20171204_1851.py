# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-04 18:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0032_articulos_resumen'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Articulos',
            new_name='Articulo',
        ),
    ]