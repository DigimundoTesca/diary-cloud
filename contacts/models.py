from django.db import models
from users.models import User


class Empresa(models.Model):
    AGUA = 'AG'
    FUEGO = 'FG'
    TIERRA = 'TR'
    AIRE = 'AR'

    TIPO = (
        (AGUA, 'agua'),
        (FUEGO, 'fuego'),
        (TIERRA, 'tierra'),
        (AIRE, 'aire'),
    )
    nombre = models.CharField(max_length=60, default='')
    giro = models.CharField(max_length=30, default='')
    tipo = models.CharField(max_length=20, default='', choices=TIPO)
    direccion = models.CharField(max_length=254, blank=True, null=True)
    web = models.URLField(default='', blank=True, null=True)

    def __str__(self):
        return '%s' % self.nombre


class Contacto(models.Model):
    SEÑOR = 'SR'
    SEÑORA  = 'SRA'
    LICENCIADO  = 'LIC'
    INGENIERO = 'ING'
    MAESTRO = 'MTR'
    DOCTOR = 'DR'

    TRATAMIENTOS = (
        (SEÑOR, 'Sr.'),
        (SEÑORA, 'Sra.'),
        (LICENCIADO, 'Lic.'),
        (INGENIERO, 'Ing.'),
        (MAESTRO, 'Mtr.'),
        (DOCTOR, 'Dr.'),
    )
    creado_por = models.ForeignKey(User)
    tratamiento = models.CharField(max_length=3, choices=TRATAMIENTOS, default=SEÑOR)
    nombre = models.CharField(max_length=90, default='')
    telefono_principal = models.CharField(max_length=12, default='') # Se sustituirá por teléfonos personales
    empresa = models.CharField(max_length=255, null=True, blank=True) #campo a eliminar, añadido en modelo empresa
    empresa_fk = models.ManyToManyField(Empresa)
    cargo = models.CharField(max_length=28, default='', blank=True, null=True)
    web_personal = models.URLField(default='', blank=True, null=True)
    email = models.EmailField(default='', blank=True, null=True)
    direccion = models.CharField(max_length=254, blank=True, null=True) # campo a eliminar, añadido en modelo empresa
    nota = models.TextField(default='', blank=True, null=True)
    imagen = models.ImageField(upload_to='contacts', null=True, blank=True)
    creado_en = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return '%s' % self.nombre
