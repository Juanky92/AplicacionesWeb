# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-29 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('micropchip', models.CharField(max_length=30)),
                ('Nombre', models.CharField(max_length=100)),
                ('Edad', models.IntegerField()),
                ('Raza', models.CharField(max_length=150)),
                ('Caracter', models.CharField(max_length=50)),
                ('Habitos', models.CharField(max_length=150)),
                ('Peso', models.IntegerField()),
                ('Vacunas', models.BooleanField()),
                ('Color', models.CharField(max_length=100)),
                ('Uso', models.CharField(max_length=100)),
                ('Altura', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='microchip', to='dog.Perro')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellidos', models.CharField(max_length=150)),
                ('Dni', models.IntegerField()),
                ('Sexo', models.CharField(max_length=10)),
                ('Telefono', models.IntegerField()),
                ('Edad', models.IntegerField()),
                ('Domicilio', models.CharField(max_length=150)),
                ('Cp', models.IntegerField()),
                ('Localidad', models.CharField(max_length=75)),
                ('Correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='propietario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dog.Usuario'),
        ),
    ]
