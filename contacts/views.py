from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Contacto, Telefono


@login_required(login_url='users:login')
def contactos(request):
    template = 'contactos.html'
    contactos_lista = Contacto.objects.all()
    telefonos_lista = Telefono.objects.all()
    context = {
        'contactos': contactos_lista,
        'telefonos': telefonos_lista
    }
    return render(request, template, context)
