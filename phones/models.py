from django.db import models
from contacts.models import Contacto
from contacts.models import Empresa


class Telefono(models.Model):
    tipo = models.CharField(max_length=24, default='', help_text='Ingresa el tipo de telefono')
    numero = models.CharField(max_length=12, default='', help_text='Ingresa un numero no mayor a 16 digitos')

    def __str__(self):
        return '%s' % self.numero


class TelefonoContacto(models.Model):
    """
    Modelo que contiene las referencias a los teléfonos de los contactos
    """
    telefono = models.ForeignKey(
        Telefono,
        on_delete=models.CASCADE,
    )
    contacto = models.ForeignKey(
        Contacto,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Teléfono del Contacto'
        verbose_name_plural  = 'Teléfonos del Contácto'



class TelefonoEmpresa(models.Model):
    """
    Modelo que contiene las referencias a los teléfonos de los contactos
    """
    telefono = models.ForeignKey(
        Telefono,
        on_delete=models.CASCADE,
    )
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE
    )
    class Meta:
        verbose_name = 'Teléfono de la Empresa'
        verbose_name_plural  = 'Teléfonos de la Empresa'
