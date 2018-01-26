from django.db import models
from users.models import User


class Empresa(models.Model):
    AGUA = 'AG'
    FUEGO = 'FG'
    TIERRA = 'TR'
    AIRE = 'AR'
    ETER = 'ET'

    ELEMENTO = (
        (AGUA, 'agua'),
        (FUEGO, 'fuego'),
        (TIERRA, 'tierra'),
        (AIRE, 'aire'),
        (ETER, 'eter')
    )

    nombre = models.CharField(max_length=60, default='')
    email = models.EmailField(default='', blank=True, null=True)
    giro = models.CharField(max_length=30, default='')
    subgiro = models.CharField(max_length=30, default='')
    elemento = models.CharField(max_length=2, default='', choices=ELEMENTO)
    tipo = models.CharField(max_length=2, default='',)
    direccion = models.CharField(max_length=254, blank=True, null=True)
   # web = models.URLField(default='', blank=True, null=True)
   # nota = models.TextField(blank=True, null=True)

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

    CERO = '0'
    UNO = '1'
    DOS = '2'
    TRES = '3'

    NIVEL = (
        (CERO, 'Dueño/Fundador'),
        (UNO, 'Socio/Director'),
        (DOS, 'Gerente/Jefe de area'),
        (TRES, 'Empleado, Analisis'),
    )

    creado_por = models.ForeignKey(User, default=0)
    tratamiento = models.CharField(max_length=3, choices=TRATAMIENTOS, default=SEÑOR)
    nombre = models.CharField(max_length=90, default='')
    email = models.EmailField(default='', blank=True, null=True)
    ntd = models.CharField(max_length=2, default=CERO, choices=NIVEL)
    nota = models.TextField(default='', blank=True, null=True)
    fecha_de_creacion = models.DateTimeField(editable=False, auto_now=True, null=True)
    telefono = models.PositiveIntegerField(blank=True, null=True)
    extension = models.PositiveSmallIntegerField(blank=True, null=True)
    celular = models.PositiveIntegerField(blank=True, null=True)
    empresa = models.ForeignKey(Empresa)
    imagen = models.ImageField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.nombre
