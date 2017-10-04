# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-02 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0009_auto_20171002_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perro',
            old_name='Altura',
            new_name='altura',
        ),
        migrations.RenameField(
            model_name='perro',
            old_name='Caracter',
            new_name='caracter',
        ),
        migrations.RenameField(
            model_name='perro',
            old_name='Color',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='perro',
            old_name='Cruze',
            new_name='cruze',
        ),
        migrations.RenameField(
            model_name='perro',
            old_name='Descripcion',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='perro',
            old_name='Edad',
            new_name='edad',
        ),
        migrations.RenameField(
            model_name='perro',
            old_name='Habitos',
            new_name='habitos',
        ),
        migrations.RenameField(
            model_name='perro',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='perro',
            old_name='Peso',
            new_name='peso',
        ),
        migrations.RenameField(
            model_name='perro',
            old_name='Raza',
            new_name='raza',
        ),
        migrations.RenameField(
            model_name='perro',
            old_name='Uso',
            new_name='uso',
        ),
        migrations.RenameField(
            model_name='perro',
            old_name='Vacunas',
            new_name='vacunas',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Apellidos',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Correo',
            new_name='correo',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Cp',
            new_name='cp',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Dni',
            new_name='dni',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Domicilio',
            new_name='domicilio',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Edad',
            new_name='edad',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Localidad',
            new_name='localidad',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Nombre',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Sexo',
            new_name='sexo',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='Telefono',
            new_name='telefono',
        ),
        migrations.AlterField(
            model_name='propiedade',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dog.Usuario'),
        ),
    ]