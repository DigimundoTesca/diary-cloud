from django.shortcuts import render
from .models import Contacto


def contactos(request):
    template = 'contactos.html'
    contactos_lista = Contacto.objects.all()
    context = {
        'contactos': contactos_lista,
    }
    return render(request, template, context)
