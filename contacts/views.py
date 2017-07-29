from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Contacto, Telefono
from .forms import ContactoForm
from django.views.generic import CreateView

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


class NuevoContacto(CreateView):
    model = Contacto
    fields = ['nombre','empresa', 'web', 'email', 'direccion', 'nota', 'imagen', 'usuario']
    template_name = 'contactos/nuevo_contacto.html'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('contactos:contactos')
