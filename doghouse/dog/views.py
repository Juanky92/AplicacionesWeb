from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from forms import UsuarioForm, UserForm
from django.contrib.auth import authenticate, login, logout

def inicio(request):
	if request.user.is_authenticated:
		return render(request, "inicio.html", {})
	else:
		return redirect("Login")

def base(request):
	return render(request,"base.html",{})

@method_decorator(login_required,name = 'dispatch' )
class perroCreate(CreateView):
	model=Perro
	fields=['microchip','nombre','edad','caracter','habitos','peso','vacunas','color','uso','altura','raza','cruce','descripcion','estado']
	success_url = reverse_lazy("Lista-de-perros")
	def form_valid(self,form):
		form.instance.propietario=User.objects.get(username=self.request.user.username)
		return super(perroCreate,self).form_valid(form)

@method_decorator(login_required,name = 'dispatch' )
class perroUpdate(UpdateView):
	model=Perro
	fields=['microchip','nombre','edad','caracter','habitos','peso','vacunas','color','uso','altura','raza','cruce','descripcion','estado']
	success_url = reverse_lazy("Lista-de-perros")


@method_decorator(login_required,name = 'dispatch' )
class perroDelete(DeleteView):
	model=Perro
	success_url = reverse_lazy("Lista-de-perros")

class perroList(ListView):
    model = Perro
    fields =['microchip','nombre','edad','caracter','habitos','peso','vacunas','color','uso','altura','raza','cruce','descripcion','estado']

    def __unicode__(self):
		return self.nombre

class razaList(ListView):
    model = Raza
    fields =['raza']

    def __unicode__(self):
		return self.raza


class perroDetail(DetailView):
	queryset=Perro.objects.all()

@method_decorator(login_required,name = 'dispatch' )
class razaDetail(DetailView):
	queryset=Raza.objects.all()


def loginView(request):
	if request.method == "POST":
		usuario = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=usuario, password=password)
		if user is not None:
			login(request, user)
			return redirect("inicio")
		else:
			return redirect("Login")
	else:
		return render(request,"login.html")

def logoutView(request):
	logout(request)
	return redirect("Login")

def UsuarioNuevo(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		usuario_form = UsuarioForm(request.POST)
	 	if user_form.is_valid() and usuario_form.is_valid():
	 		new_user = User.objects.create_user(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'],email=user_form.cleaned_data['email'],first_name=user_form.cleaned_data['first_name'],last_name=user_form.cleaned_data['last_name'])
	 		new_user.usuario.dni = usuario_form.cleaned_data['dni']
			new_user.usuario.sexo=usuario_form.cleaned_data['sexo']
			new_user.usuario.telefono=usuario_form.cleaned_data['telefono']
			new_user.usuario.edad=usuario_form.cleaned_data['edad']
			new_user.usuario.domicilio=usuario_form.cleaned_data['domicilio']
			new_user.usuario.cp=usuario_form.cleaned_data['cp']
			new_user.usuario.localidad=usuario_form.cleaned_data['localidad']
			new_user.save()
	 		return redirect('inicio')
	 	else:
	 		print "No es correcto"
	else:
	 	user_form = UserForm()
	 	usuario_form = UsuarioForm()
	return render(request, "dog/user_form.html",{'user_form': user_form,'usuario_form': usuario_form})
