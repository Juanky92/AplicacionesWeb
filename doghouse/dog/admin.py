from django.contrib import admin

# Register your models here.

from .models import (Usuario,Perro,Propiedade,Raza)

admin.site.register(Usuario)
admin.site.register(Perro)
admin.site.register(Propiedade)
admin.site.register(Raza)