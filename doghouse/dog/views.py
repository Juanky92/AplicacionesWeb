from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth import authenticate, login, logout

def inicio(request):
	if request.user.is_authenticated:
		return render(request, "inicio.html", {})
	else:
		return redirect("Login")

class perroCreate(CreateView):
	model=Perro
	fields=['microchip','nombre','edad','caracter','habitos','peso','vacunas','color','uso','altura','raza','cruce','descripcion','estado']
	success_url = reverse_lazy("Lista-de-perros")

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
class razaDetail(DetailView):
	queryset=Raza.objects.all()
class propiedadeDetail(DetailView):
	queryset=Propiedade.objects.all()

def loginView(request):
	if request.method == "POST":
		usuario = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=usuario, password=password)
		if user is not None:
			login(request, user)
			return redirect("inicio")
	else:
		return render(request,"login.html")

def logoutView(request):
	logout(request)
	return redirect("Login")