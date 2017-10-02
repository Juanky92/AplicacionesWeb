from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Raza(models.Model):
	Raza=models.CharField(max_length=150)
	def __unicode__(self):
		return self.Raza

class Perro(models.Model):
	micropchip=models.CharField(max_length=30,unique=True)
	Nombre=models.CharField(max_length=100)
	Edad=models.IntegerField()
	#foto=models.ImageField(upload_to=None,blank=True)
	Caracter=models.CharField(max_length=50)
	Habitos=models.CharField(max_length=150)
	Peso=models.IntegerField()
	Vacunas=models.BooleanField()
	Color=models.CharField(max_length=100)
	Uso=models.CharField(max_length=100)
	Altura=models.CharField(max_length=50)
	Raza=models.ForeignKey(Raza)
	Cruze=models.BooleanField()
	Descripcion=models.CharField(max_length=150,blank=True)
	def __unicode__(self):
		return self.Nombre

class Usuario(models.Model):
	Hombre='H'
	Mujer='M'
	Nombre=models.CharField(max_length=50)
	Apellidos=models.CharField(max_length=150)
	Dni=models.IntegerField()
	Sexo_choices=(('H','Hombre'),('M','Mujer'),)
	Sexo=models.CharField(max_length=2,choices=Sexo_choices,default=Hombre,)
	Telefono=models.IntegerField()
	Edad=models.IntegerField()
	Domicilio=models.CharField(max_length=150)
	Cp=models.IntegerField()
	Localidad=models.CharField(max_length=75)
	Correo=models.EmailField()

	def __unicode__(self):
			return self.Correo

class Propiedade(models.Model):
	perro=models.OneToOneField(Perro,related_name='microchip')
	usuario=models.OneToOneField(Usuario,related_name='correo')


