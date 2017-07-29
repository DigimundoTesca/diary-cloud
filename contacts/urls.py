from django.conf.urls import url, include

from . import views
from .views import NuevoContacto

app_name = 'contactos'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contactos/$', views.contactos, name='contactos'),
    url(r'^contactos/nuevo/$', NuevoContacto.as_view(), name='nuevo_contacto')
]
