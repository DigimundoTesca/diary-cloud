from django.db import models
from users.models import User


class Contacto(models.Model):
    nombre = models.CharField(max_length=60, default='')
    telefono_principal = models.CharField(max_length=12, default='')
    empresa = models.CharField(max_length=90, default='', blank=True, null=True)
    cargo = models.CharField(max_length=28, default='', blank=True, null=True)
    web = models.URLField(default='', blank=True, null=True)
    email = models.EmailField(default='', blank=True, null=True)
    direccion = models.CharField(max_length=254, blank=True, null=True)
    nota = models.TextField(default='', blank=True, null=True)
    imagen = models.ImageField(upload_to='contacts', null=True, blank=True)
    usuario = models.ForeignKey(User)

    def __str__(self):
        return '%s' % self.nombre

    def telefono(self):
        telefonos = Telefono.objects.filter(contacto=self.id)
        options = []

        for tel in telefonos:
            options.append(("<option value=%s selected>%s</option>" % (tel, tel)))
        tag = """<select>%s</select>""" % str(options)
        return tag

    telefono.allow_tags = True


class Telefono(models.Model):
    tipo = models.CharField(max_length=24, default='', help_text='Ingresa el tipo de telefono')
    numero = models.CharField(max_length=12, default='', help_text='Ingresa un numero no mayor a 16 digitos')
    contacto = models.ForeignKey(Contacto)

    def __str__(self):
        return '%s' % self.numero
