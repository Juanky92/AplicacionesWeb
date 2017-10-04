from django.shortcuts import render
from .forms import UsuarioForm,PerroForm
from .models import Usuario,Perro,Propiedade,Raza
# Create your views here.
def inicio(request):
	return render(request,"inicio.html",{})

def usuario(request):
	form=UsuarioForm(request.POST or None)
	if form.is_valid():
		form_data=form.cleaned_data
		abc=form_data.get('nombre')
		abc2=form_data.get('apellidos')
		abc3=form_data.get('dni')
		abc4=form_data.get('sexo')
		abc5=form_data.get('telefono')
		abc6=form_data.get('edad')
		abc7=form_data.get('domicilio')
		abc8=form_data.get('cp')
		abc9=form_data.get('localidad')
		abc10=form_data.get('correo')
		obj=Usuario.objects.create(nombre=abc,apellidos=abc2,dni=abc3,sexo=abc4,telefono=abc5,edad=abc6,domicilio=abc7,cp=abc8,localidad=abc9,correo=abc10)
	context={"el_form":form,}
	return render(request,"usuario.html",context)

def perro(request):
	form=PerroForm(request.POST or None)
	if form.is_valid():
		form_data=form.cleaned_data
		abc=form_data.get('microchip')
		abc2=form_data.get('nombre')
		abc3=form_data.get('edad')
		abc4=form_data.get('caracter')
		abc5=form_data.get('habitos')
		abc6=form_data.get('peso')
		abc7=form_data.get('vacunas')
		abc8=form_data.get('color')
		abc9=form_data.get('uso')
		abc10=form_data.get('altura')
		abc11=form_data.get('raza')
		abc12=form_data.get('cruze')
		abc13=form_data.get('descripcion')
		abc14=form_data.get('estado')
		obj=Perro.objects.create(microchip=abc,nombre=abc2,edad=abc3,caracter=abc4,habitos=abc5,peso=abc6,vacunas=abc7,color=abc8,uso=abc9,altura=abc10,raza=abc11,cruze=abc12,descripcion=abc13,estado=abc14)
	context={"ele_form":form,}
	return render(request,"perro.html",context)
