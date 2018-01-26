from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


from .models import Contacto
from users.models import User


class ContactoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)
        self.fields['creado_por'].widget.attrs.update({'class': 'hidden'})
        self.fields['tipo'].widget.attrs.update({'class': 'hidden'})

    class Meta:
        model = Contacto
        fields = (
            'creado_por',
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
            'giro',
            'cargo',
            'tipo',
        )
        labels = {
            'creado_por': '',
            'tratamiento': 'Tratamiento',
            'nombre': 'Nombre',
            'email': 'E-mail',
            'ntd': 'Nivel de Toma de Desiciones',
            'telefono': 'Telefono',
            'extension': 'Extension',
            'celular': 'Celular',
            'empresa': 'Empresa',
            'nota': 'Nota',
            'imagen': '',
            'giro': 'Giro',
            'cargo': 'Cargo',
            'tipo': '',
        }
