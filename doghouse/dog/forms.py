from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from models import Usuario, Perro

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['dni','sexo','telefono','edad','domicilio','cp','localidad']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password','email','first_name','last_name']
        help_text = None

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = ['microchip','nombre','edad','caracter','foto','habitos','peso','vacunas','color','uso','altura','raza','cruce','descripcion','estado']