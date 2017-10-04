# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-02 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0010_auto_20171002_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='foto',
            field=models.ImageField(blank=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='propiedade',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='email', to='dog.Usuario'),
        ),
    ]