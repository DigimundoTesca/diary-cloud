from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Contacto, Telefono
from .forms import ContactoForm

def home(request):
    template = 'home.html'
    context = {}
    return render(request, template, context)


@login_required()
def contactos(request):
    template = 'contactos/contactos.html'
    contactos_lista = Contacto.objects.all()
    telefonos_lista = Telefono.objects.all()
    context = {
        'contactos': contactos_lista,
        'telefonos': telefonos_lista
    }
    return render(request, template, context)


@login_required()
def nuevo_contacto(request):
    form = ContactoForm
    template = 'contactos/nuevo_contacto.html'
    context = {
    'form': form
    }
    return render(request, template, context)
