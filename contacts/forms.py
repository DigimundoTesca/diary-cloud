from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


from .models import Contacto
from users.models import User


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = (
            'tratamiento',
            'nombre',
            'email',
            'ntd',
            'telefono',
            'extension',
            'empresa',
            'nota',
            'celular',
            'imagen',
        )
        labels = {
            'tratamiento': 'Tratamiento',
            'nombre': 'Nombre',
            'email': 'E-mail',
            'ntd': 'Nivel de Toma de Desiciones',
            'telefono': 'Telefono',
            'extension': 'Extension',
            'celular': 'Celular',
            'empresa': 'Empresa',
            'nota': 'Nota',
            'imagen': 'Fotografia',
        }
