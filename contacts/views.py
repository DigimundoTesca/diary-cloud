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
    context = {
        'contactos': contactos_lista,
    }
    return render(request, template, context)

@login_required()
def nuevoContacto(request):
    template = 'contactos/nuevo_contacto.html'
    form = ContactoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            base = form.save(commit=False)
            base.creado_por = request.user
            base.tipo = get_elemement(base.giro)
            base.save()
            return redirect('contactos:nuevo_contacto')
        else:
            print(form.is_valid())
            print(form.errors)
    context = {
        'form': form,
    }
    return render(request, template, context)


def get_elemement(giro):
    agua = ['CC', 'DH', 'ED', 'AP', 'RS', 'BN', 'SL', 'AAG']
    #Fuego
    fuego = ['IBIT', 'SG', 'CN', 'EC', 'FE', 'AF']
    #Aire
    aire = ['CON', 'PRM', 'DF', 'MRD', 'IMP', 'UNI', 'IMP', 'DEC', 'DSG', 'ANP', 'FTG', 'ETM', 'AA']
    #Tierra
    tierra = ['COPR', 'EQCO', 'ECOC', 'EQEL', 'EQOF', 'BIRA', 'FERRE', 'MAPR', 'SFTW', 'DIIN', 'INEL', 'INPL', 'MNTN',
              'PRQU', 'ARQI', 'INGC', 'DIIN', 'SGRD', 'SISA', 'AT']

    if giro in fuego:
        return 'FG'
    elif giro in agua:
        return 'AG'
    elif giro in aire:
        return 'AR'
    elif giro in tierra:
        return 'TR'
    else:
        return 'ET'

