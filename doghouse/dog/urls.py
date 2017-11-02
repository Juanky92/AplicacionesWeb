from django.conf.urls import url, include
from dog import views
from dog.views import *

from . import views
    
urlpatterns = [
    url(r'^inicio$', views.inicio, name='inicio'),
    url(r'^nuevo/$', UsuarioNuevo, name='Usuario'),
    url(r'^perro_list/$',perroList.as_view(),name="Lista-de-perros"),
    url(r'^raza_list/$',razaList.as_view(),name="Lista-de-razas"),
    url(r'^perro_list/(?P<pk>[0-9]+)/$',perroDetail.as_view(),name="Detalle-de-perro"),
    url(r'^raza_list/(?P<pk>[0-9]+)/$',razaDetail.as_view(),name="Detalle-de-raza"),
    url(r'perro_form/add/$', perroCreate.as_view(), name='perro_add'),
    url(r'perro_form/(?P<pk>[0-9]+)/$', perroUpdate.as_view(), name='perro_update'),
    url(r'perro_list/perro_confirm_delete/(?P<pk>[0-9]+)/delete/$', perroDelete.as_view(), name='perro_delete'),
    url(r'^login/$', views.loginView, name="Login"),
    url(r'^logout/$', views.logoutView, name="Logout"),
]