from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from dog import views
from dog.views import *

from . import views

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^inicio$', views.inicio, name='inicio'),
    url(r'^nuevo/$', UsuarioNuevo, name='Usuario'),
    url(r'^perro_list/$',perroList.as_view(),name="Lista-de-perros"),
    url(r'^raza_list/$',razaList.as_view(),name="Lista-de-razas"),
    url(r'^perro_list/(?P<pk>[0-9]+)/$',perroDetail.as_view(),name="Detalle-de-perro"),
    url(r'^raza_list/(?P<pk>[0-9]+)/$',razaDetail.as_view(),name="Detalle-de-raza"),
    url(r'perro_form/add/$', perroCreate, name='perro_add'),
    url(r'perro_form/(?P<pk>[0-9]+)/$', perroUpdate.as_view(), name='perro_update'),
    url(r'perro_list/perro_confirm_delete/(?P<pk>[0-9]+)/delete/$', perroDelete.as_view(), name='perro_delete'),
    url(r'^login/$', views.loginView, name="Login"),
    url(r'^logout/$', views.logoutView, name="Logout"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^articulo_list/$',ArticuloList.as_view(),name="ArticuloList"),
    url(r'^articulo_list/(?P<pk>[0-9]+)/$',ArticuloDetail.as_view(),name="ArticuloDetail"),
    url(r'articulo_form/add/$', ArticuloCreate.as_view(), name='ArticuloCreate'),
]