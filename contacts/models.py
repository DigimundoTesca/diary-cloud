from django.db import models


class Contacto(models.Model):
    nombre = models.CharField(max_length=124, default='')
    empresa = models.CharField(max_length=48, default='')
    web = models.URLField(default='', blank=True, null=True)
    email = models.EmailField(default='')
    direccion = models.CharField(max_length=254, blank=True, null=True)
    nota = models.TextField(default='')
    imagen = models.ImageField(null=True, blank=True)


class Telefono(models.Model):
    tipo = models.CharField(max_length=24, default='', help_text='Ingresa el tipo de telefono')
    numero = models.CharField(max_length=16, default='', help_text='Ingresa un numero no mayor a 16 digitos')
    contacto = models.ForeignKey(Contacto)

