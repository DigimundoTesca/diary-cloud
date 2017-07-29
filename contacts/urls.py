from django.conf.urls import url, include

from . import views


app_name = 'contactos'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contactos/$', views.contactos, name='contactos'),
    url(r'^contactos/nuevo/$', views.nuevo_contacto, name='nuevo_contacto')
]
