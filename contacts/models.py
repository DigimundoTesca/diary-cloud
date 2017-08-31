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
    email = models.EmailField(default='', blank=True, null=True)
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
    telefono_principal = models.CharField(max_length=12, default='')  # Se sustituirá por teléfonos personales
    direccion = models.CharField(max_length=254, blank=True, null=True)  # campo a eliminar, añadido en modelo empresa
    email = models.EmailField(default='', blank=True, null=True)
    empresa = models.CharField(max_length=255, null=True, blank=True)  # campo a eliminar, añadido en modelo empresa
    empresa_fk = models.ManyToManyField(Empresa)
    cargo = models.CharField(max_length=28, default='', blank=True, )
    web_personal = models.URLField(default='', blank=True, null=True)
    nota = models.TextField(default='', blank=True, null=True)
    imagen = models.ImageField(upload_to='contacts', blank=True, null=True)
    fecha_de_creacion = models.DateTimeField(editable=False, auto_now=True, null=True)

    def __str__(self):
        return '%s' % self.nombre
