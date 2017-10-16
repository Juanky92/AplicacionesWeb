from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
#from .forms import UsuarioForm,PerroForm
from django.urls import reverse_lazy
from .models import Usuario,Perro,Propiedade,Raza
# Create your views here.
def inicio(request):
	return render(request,"inicio.html",{})

class perroCreate(CreateView):
	model=Perro
	fields=['microchip','nombre','edad','caracter','habitos','peso','vacunas','color','uso','altura','raza','cruce','descripcion','estado']
	success_url = reverse_lazy("Lista-de-perros")

class usuarioCreate(CreateView):
	model=Usuario
	fields =['nombre','apellidos','dni','sexo','telefono','edad','domicilio','cp','localidad','correo']
	success_url = reverse_lazy("Lista-de-usuarios")

class razaCreate(CreateView):
	model=Raza
	fields =['raza']
	success_url = reverse_lazy("Lista-de-razas")

class propiedadeCreate(CreateView):
	model=Propiedade
	fields =['perro','usuario']
	success_url = reverse_lazy("Lista-de-propiedad")


class perroUpdate(UpdateView):
	model=Perro
	fields=['microchip','nombre','edad','caracter','habitos','peso','vacunas','color','uso','altura','raza','cruce','descripcion','estado']
	success_url = reverse_lazy("Lista-de-perros")

class usuarioUpdate(UpdateView):
	model=Usuario
	fields =['nombre','apellidos','dni','sexo','telefono','edad','domicilio','cp','localidad','correo']
	success_url = reverse_lazy("Lista-de-usuarios")

class razaUpdate(UpdateView):
	model=Raza
	fields =['raza']
	success_url = reverse_lazy("Lista-de-razas")

class propiedadeUpdate(UpdateView):
	model=Propiedade
	fields =['perro','usuario']
	success_url = reverse_lazy("Lista-de-propiedad")

class perroDelete(DeleteView):
	model=Perro
	success_url = reverse_lazy("Lista-de-perros")

class usuarioDelete(DeleteView):
	model=Usuario
	success_url = reverse_lazy("Lista-de-usuarios")

class razaDelete(DeleteView):
	model=Raza
	success_url = reverse_lazy("Lista-de-razas")

class propiedadeDelete(DeleteView):
	model=Propiedade
	success_url = reverse_lazy("Lista-de-propiedad")


class perroList(ListView):
    model = Perro
    fields =['microchip','nombre','edad','caracter','habitos','peso','vacunas','color','uso','altura','raza','cruce','descripcion','estado']

    def __unicode__(self):
		return self.nombre

class usuarioList(ListView):
    model = Usuario
    fields =['nombre','apellidos','dni','sexo','telefono','edad','domicilio','cp','localidad','correo']

    def __unicode__(self):
		return self.nombre

class razaList(ListView):
    model = Raza
    fields =['raza']

    def __unicode__(self):
		return self.raza

class propiedadesList(ListView):
    model = Propiedade
    fields =['perro','usuario']

    def __unicode__(self):
		return self.str(usuario)

class perroDetail(DetailView):
	queryset=Perro.objects.all()
class usuarioDetail(DetailView):
	queryset=Usuario.objects.all()
class razaDetail(DetailView):
	queryset=Raza.objects.all()
class propiedadeDetail(DetailView):
	queryset=Propiedade.objects.all()

