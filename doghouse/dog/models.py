from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Raza(models.Model):
	raza=models.CharField(max_length=150)
	def __unicode__(self):
		return self.raza

class Perro(models.Model):
	adoptable='A'
	adoptado='AD'
	enano="e"
	mediano="m"
	grande="g"
	microchip=models.CharField(max_length=30,unique=True)
	nombre=models.CharField(max_length=100)
	edad=models.IntegerField()
	#foto=models.ImageField(upload_to='imagen/',blank=True)
	caracter=models.CharField(max_length=50)
	habitos=models.CharField(max_length=150)
	peso=models.IntegerField()
	vacunas=models.BooleanField()
	color=models.CharField(max_length=100)
	uso=models.CharField(max_length=100)
	altura_choices=(('e','enano'),('m','mediano'),('g','grande'))
	altura=models.CharField(max_length=3,choices=altura_choices,default=mediano,)
	raza=models.ForeignKey(Raza)
	cruce=models.BooleanField()
	descripcion=models.CharField(max_length=150,blank=True)
	estado_choices=(('A','adoptable'),('AD','adoptado'),)
	estado=models.CharField(max_length=2,choices=estado_choices,default=adoptable,)
	def __unicode__(self):
		return self.nombre

class Usuario(models.Model):
	hombre='H'
	mujer='M'
	nombre=models.CharField(max_length=50)
	apellidos=models.CharField(max_length=150)
	dni=models.CharField(max_length=9)
	sexo_choices=(('H','Hombre'),('M','Mujer'),)
	sexo=models.CharField(max_length=2,choices=sexo_choices,default=hombre,)
	telefono=models.CharField(max_length=15)
	edad=models.CharField(max_length=2)
	domicilio=models.CharField(max_length=150)
	cp=models.CharField(max_length=10)
	localidad=models.CharField(max_length=75)
	correo=models.EmailField()

	def __unicode__(self):
			return self.correo

class Propiedade(models.Model):
	perro=models.ForeignKey(Perro,unique=True)
	usuario=models.ForeignKey(Usuario)
	
	def __unicode__(self):
			return str(self.usuario)+" "+" "+" "+str(self.perro)
