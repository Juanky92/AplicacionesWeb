# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-29 19:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0007_auto_20170929_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propiedade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='microchip', to='dog.Perro')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='correo', to='dog.Usuario')),
            ],
        ),
        migrations.RemoveField(
            model_name='propietario',
            name='perro',
        ),
        migrations.RemoveField(
            model_name='propietario',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Propietario',
        ),
    ]
