from django.conf.urls import url, include

from . import views


app_name = 'contactos'

urlpatterns = [
    url(r'^contactos/$', views.contactos, name='contactos')
]
