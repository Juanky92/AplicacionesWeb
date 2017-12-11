from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import os


def path_and_renames(instance, filename):
	upload_to = settings.MEDIA_ROOT + "/razas"
	ext = filename.split('.')[-1]
	# get filename
	if instance.pk:
		filename = '{}.{}'.format(instance.pk, "jpg")
	# return the whole path to the file
	return os.path.join(upload_to, filename)

class Raza(models.Model):
	raza=models.CharField(max_length=150)
	descripcion=models.TextField(max_length=5000, null=True)
	imagen=models.ImageField(upload_to=path_and_renames, null=True)
	def __unicode__(self):
		return self.raza
	def get_absolute_url(self):
		return reverse('raza_detail',kwargs={'pk':self.pk})
	# Override del save() por defecto.
	def save(self, *args, **kwargs):
		if self.pk is None:
			foto = self.imagen
			self.imagen = None
			super(Raza, self).save(*args, **kwargs)
			self.imagen = foto
			kwargs.pop('force_insert')
		super(Raza, self).save(*args, **kwargs)


class Usuario(models.Model):
	hombre='H'
	mujer='M'
	dni=models.CharField(max_length=9)
	sexo_choices=(('H','Hombre'),('M','Mujer'),)
	sexo=models.CharField(max_length=2,choices=sexo_choices,default=hombre,)
	telefono=models.CharField(max_length=15)
	edad=models.CharField(max_length=2)
	domicilio=models.CharField(max_length=150)
	cp=models.CharField(max_length=10)
	localidad=models.CharField(max_length=75)
	usuario=models.OneToOneField(User,on_delete=models.CASCADE,unique=True)

	@receiver(post_save, sender=User)
	def create_user_usuario(sender, instance, created, **kwargs):
		if created:
			Usuario.objects.create(usuario=instance)

	@receiver(post_save, sender=User)
	def save_user_usuario(sender, instance, **kwargs):
		instance.usuario.save()


	def __unicode__(self):
		return str(self.usuario)

	def get_absolute_url(self):
		return reverse('usuario_detail',kwargs={'pk':self.pk})

def path_and_renamese(instance, filename):
	upload_to = settings.MEDIA_ROOT
	ext = filename.split('.')[-1]
	if instance.pk:
		filename = '{}.{}'.format(instance.pk, "jpg")
	return os.path.join(upload_to, filename)

class Perro(models.Model):
	adoptable='A'
	adoptado='AD'
	enano="e"
	mediano="m"
	grande="g"
	microchip=models.CharField(max_length=30,unique=True)
	nombre=models.CharField(max_length=100)
	edad=models.IntegerField()
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
	propietario=models.ForeignKey(User)
	foto=models.ImageField(upload_to=path_and_renamese, null=True)

	# Override del save() por defecto.
	def save(self, *args, **kwargs):
		if self.pk is None:
			imagen = self.foto
			self.foto = None
			super(Perro, self).save(*args, **kwargs)
			self.foto = imagen
			kwargs.pop('force_insert')
		super(Perro, self).save(*args, **kwargs)
	

	def __unicode__(self):
		return self.nombre
	def get_absolute_url(self):
		return reverse('perro_detail',kwargs={'pk':self.pk})

class Articulo(models.Model):
	titulo=models.CharField(max_length=100)
	contenido=models.TextField(max_length=5000)
	resumen=models.TextField(max_length=300)
	def __unicode__(self):
		return self.titulo
	def get_absolute_url(self):
		return reverse('articulo_detail',kwargs={'pk':self.pk})