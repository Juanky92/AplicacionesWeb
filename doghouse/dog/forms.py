from django import forms

from .models import Raza,Perro,Propiedade,Usuario
class UsuarioForm(forms.ModelForm):
	class Meta:
		model=Usuario
		fields=['nombre','apellidos','dni','sexo','telefono','edad','domicilio','cp','localidad','correo']

class PerroForm(forms.ModelForm):
	class Meta:
		model=Perro
		fields=['microchip','nombre','edad','caracter','habitos','peso','vacunas','color','uso','altura','raza','cruce','descripcion','estado']

