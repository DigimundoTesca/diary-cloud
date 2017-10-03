from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from .models import Contacto
from .models import Empresa
from phones.models import Telefono
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
    empresa_lista = Empresa.objects.all()
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect()
    else:
        form = ContactoForm()
    context = {
        'contactos': contactos_lista,
        'telefonos': telefonos_lista,
        'empresa': empresa_lista,
        'form': form,
    }
    return render(request, template, context)


class NuevoContacto(CreateView):
    model = Contacto
    fields = [
        'nombre',
        'empresa',
        'cargo',
        'telefono_principal',
        'email',
        'direccion',
        'web',
        'nota',
        'imagen',
        'usuario',
    ]
    template_name = 'contactos/nuevo'

    def form_valid(self, form):
        self.object = form.save()
        return redirect('contactos:contactos')
