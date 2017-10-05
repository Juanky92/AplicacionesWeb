"""doghouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from dog import views
from dog.views import perroList, usuarioList, razaList, propiedadesList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^perro_list/$',perroList.as_view(),name="Lista-de-perros"),
    url(r'^usuario_list/$',usuarioList.as_view(),name="Lista-de-usuarios"),
    url(r'^raza_list/$',razaList.as_view(),name="Lista-de-razas"),
    url(r'^propiedade_list/$',propiedadesList.as_view(),name="Lista-de-propiedad"),
    #url(r'^usuario/$', views.usuario, name='usuario'),


]
