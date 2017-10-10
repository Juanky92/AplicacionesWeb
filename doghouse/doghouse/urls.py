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
from dog.views import perroList, usuarioList, razaList, propiedadesList,perroDetail,usuarioDetail,propiedadeDetail,razaDetail,usuarioCreate,perroCreate,propiedadeCreate,razaCreate,usuarioUpdate,perroUpdate,propiedadeUpdate,razaUpdate,usuarioDelete,perroDelete,propiedadeDelete,razaDelete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^perro_list/$',perroList.as_view(),name="Lista-de-perros"),
    url(r'^usuario_list/$',usuarioList.as_view(),name="Lista-de-usuarios"),
    url(r'^raza_list/$',razaList.as_view(),name="Lista-de-razas"),
    url(r'^propiedade_list/$',propiedadesList.as_view(),name="Lista-de-propiedad"),
    url(r'^perro_list/(?P<pk>[0-9]+)/$',perroDetail.as_view(),name="Detalle-de-perro"),
    url(r'^usuario_list/(?P<pk>[0-9]+)/$',usuarioDetail.as_view(),name="Detalle-de-usuario"),
    url(r'^raza_list/(?P<pk>[0-9]+)/$',razaDetail.as_view(),name="Detalle-de-raza"),
    url(r'propiedade_list/(?P<pk>[0-9]+)/$',propiedadeDetail.as_view(),name="Detalle-de-propiedades"),
    url(r'usuario_form/add/$', usuarioCreate.as_view(), name='usuario_add'),
    url(r'perro_form/add/$', perroCreate.as_view(), name='perro_add'),
    url(r'raza_form/add/$', razaCreate.as_view(), name='raza_add'),
    url(r'propiedade_form/add/$', propiedadeCreate.as_view(), name='propiedade_add'),
    url(r'usuario_form/(?P<pk>[0-9]+)/$', usuarioUpdate.as_view(), name='usuario_update'),
    url(r'perro_form/(?P<pk>[0-9]+)/$', perroUpdate.as_view(), name='perro_update'),
    url(r'raza_form/(?P<pk>[0-9]+)/$', razaUpdate.as_view(), name='raza_update'),
    url(r'propiedade_form/(?P<pk>[0-9]+)/$', propiedadeUpdate.as_view(), name='propiedade_update'),
    url(r'usuario_list/usuario_confirm_delete/(?P<pk>[0-9]+)/delete/$', usuarioDelete.as_view(), name='usuario_delete'),
    url(r'perro_list/perro_confirm_delete/(?P<pk>[0-9]+)/delete/$', perroDelete.as_view(), name='perro_delete'),
    url(r'raza_list/raza_confirm_delete/(?P<pk>[0-9]+)/delete/$', razaDelete.as_view(), name='raza_delete'),
    url(r'propiedade_list/propiedade_confirm_delete/(?P<pk>[0-9]+)/delete/$', propiedadeDelete.as_view(), name='propiedade_delete'),
    #url(r'^usuario/$', views.usuario, name='usuario'),


]
