from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = [
            'tratamiento',
            'nombre',
            'email',
            'empresa',
            'cargo',
            'web_personal',
            'nota',
            'imagen',
            'fecha_de_creacion',
            'usuario',
        ]
        labels = {
            'tratamiento': 'Tratamiento',
            'nombre': 'Nombre',
            'email': 'Email',
            'empresa': 'Empresa',
            'cargo': 'Cargo',
            'web_personal': 'WebPersonal',
            'nota': 'Nota',
            'imagen': 'Imagen',
            'fecha_de_creacion': 'Fecha',
            'usuario': 'Usuario',
        }
        widgets = {
            'tratamiento': forms.Select(),
            'nombre': forms.TextInput(),
            'email': forms.EmailField(),
            'empresa': forms.Select(),
            'cargo': forms.TextInput(),
            'web_personal': forms.URLField(),
            'nota': forms.Textarea(),
            'imagen': forms.ImageField(),
            'fecha_de_creacion': forms.DateField(),
            'usuario': forms.TextInput(),
        }
