from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

from .models import (Usuario,Perro,Raza)

class UsuarioInline(admin.StackedInline):
  	model= Usuario
  	can_delete=False
  	verbose_name_plurar='Usuario'
  	fk_name='usuario'

class CustomUserAdmin(UserAdmin):
 	inlines=(UsuarioInline,)

 	def get_inline_instances(self, request, obj=None):
 		if not obj:
 			return list()
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Perro)
admin.site.register(Raza)