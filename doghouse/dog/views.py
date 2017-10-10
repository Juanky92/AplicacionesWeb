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

class usuarioCreate(CreateView):
	model=Usuario
	fields =['nombre','apellidos','dni','sexo','telefono','edad','domicilio','cp','localidad','correo']

class razaCreate(CreateView):
	model=Raza
	fields =['raza']

class propiedadeCreate(CreateView):
	model=Propiedade
	fields =['perro','usuario']


class perroUpdate(UpdateView):
	model=Perro
	fields=['microchip','nombre','edad','caracter','habitos','peso','vacunas','color','uso','altura','raza','cruce','descripcion','estado']

class usuarioUpdate(UpdateView):
	model=Usuario
	fields =['nombre','apellidos','dni','sexo','telefono','edad','domicilio','cp','localidad','correo']

class razaUpdate(UpdateView):
	model=Raza
	fields =['raza']

class propiedadeUpdate(UpdateView):
	model=Propiedade
	fields =['perro','usuario']

class perroDelete(DeleteView):
	model=Perro
	success_url = reverse_lazy('perro_list')

class usuarioDelete(DeleteView):
	model=Usuario
	success_url = reverse_lazy('usuario_list')

class razaDelete(DeleteView):
	model=Raza
	success_url = reverse_lazy('raza_list')

class propiedadeDelete(DeleteView):
	model=Propiedade
	success_url = reverse_lazy('propiedade_list')


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

#def usuario(request):
	#form=UsuarioForm(request.POST or None)
	#if form.is_valid():
		#form_data=form.cleaned_data
		#abc=form_data.get('nombre')
		#abc2=form_data.get('apellidos')
		#abc3=form_data.get('dni')
		#abc4=form_data.get('sexo')
		#abc5=form_data.get('telefono')
		#abc6=form_data.get('edad')
		#abc7=form_data.get('domicilio')
		#abc8=form_data.get('cp')
		#abc9=form_data.get('localidad')
		#abc10=form_data.get('correo')
		#obj=Usuario.objects.create(nombre=abc,apellidos=abc2,dni=abc3,sexo=abc4,telefono=abc5,edad=abc6,domicilio=abc7,cp=abc8,localidad=abc9,correo=abc10)
	#context={"el_form":form,}
	#return render(request,"usuario.html",context)

#def perro(request):
	#form=PerroForm(request.POST or None)
	#if form.is_valid():
		#form_data=form.cleaned_data
		#abc=form_data.get('microchip')
		#abc2=form_data.get('nombre')
		#abc3=form_data.get('edad')
		#abc4=form_data.get('caracter')
		#abc5=form_data.get('habitos')
		#abc6=form_data.get('peso')
		#abc7=form_data.get('vacunas')
		#abc8=form_data.get('color')
		#abc9=form_data.get('uso')
		#abc10=form_data.get('altura')
		#abc11=form_data.get('raza')
		#abc12=form_data.get('cruze')
		#abc13=form_data.get('descripcion')
		#abc14=form_data.get('estado')
		#obj=Perro.objects.create(microchip=abc,nombre=abc2,edad=abc3,caracter=abc4,habitos=abc5,peso=abc6,vacunas=abc7,color=abc8,uso=abc9,altura=abc10,raza=abc11,cruze=abc12,descripcion=abc13,estado=abc14)
	#context={"ele_form":form,}
	#return render(request,"perro.html",context)
