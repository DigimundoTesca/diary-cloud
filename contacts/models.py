from django.db import models
from users.models import User
from django.core.validators import RegexValidator


class Empresa(models.Model):

    nombre = models.CharField(max_length=60, default='')
    email = models.EmailField(default='', blank=True, null=True)
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
        (CERO, 'Dueño/Fundador (0)'),
        (UNO, 'Socio/Director (1)'),
        (DOS, 'Gerente/Jefe de area (2)'),
        (TRES, 'Empleado, Analisis (3)'),
    )

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

    COAUCHING = 'CC'
    DH = 'DH'
    EDUCACION = 'ED'
    AP = 'AP'
    RESTAURANTES = 'RS'
    BIENESTAR = 'BN'
    SALUD = 'SL'
    AAG = 'AAG'
    #Fuego
    IBIT = 'IBIT'
    SEGUROS = 'SG'
    CONTADORES = 'CN'
    ECONOMIA = 'EC'
    FE = 'FE'
    AF = 'AF'
    #Aire
    CONSULTORES = 'CON'
    PROMO = 'PRM'
    DIFUSION = 'DF'
    MARKETING = 'MRD'
    IMPRENTA = 'IMP'
    UNIFORMES = 'UNI'
    IMAGEN = 'IMP'
    DECORACION = 'DEC'
    DISEÑOG = 'DSG'
    ANUNCIOSP = 'ANP'
    FOTOGRAFIA = 'FTG'
    ESTUDIOSM = 'ETM'
    AA = 'AA'
    #Tierra
    CONSULTORESPROCESOS = 'COPR'
    EQCOMPUTO = 'EQCO'
    EQCOCINA = 'ECOC'
    EQELECTRONICOS = 'EQEL'
    EQOFICINA = 'EQOF'
    BIENESRAICES = 'BIRA'
    FERRETERIA = 'FERRE'
    MATERIASPRIMAS = 'MAPR'
    DSOFTWARE = 'SFTW'
    DISEÑOINDUSTRIAL = 'DIIN'
    INSELECTRECTRICAS = 'INEL'
    INSPLUVIALES = 'INPL'
    MANTENIMIENTO = 'MNTN'
    PRODQUIMICOS = 'PRQU'
    ARQUITECTURA = 'ARQI'
    INGCIVIL = 'INGC'
    DISEÑOINTERIORES = 'DIIN'
    SEGURIDAD = 'SGRD'
    SISTEMASAMIN = 'SISA'
    AT = 'AT'

    GIRO = (
        (IBIT, 'Inversiones BIT'),#Fuego
        (SEGUROS, 'Seguros'),
        (CONTADORES, 'Contadores'),
        (ECONOMIA, 'Economía'),
        (FE, 'Facturación Electrónica'),
        (AF, 'Asesoria Fuego'),
        #Aire
        (CONSULTORES, 'Consultores/Agencia'),
        (PROMO, 'Promocionales'),
        (DIFUSION, 'Difusión'),
        (MARKETING, 'Marketing Digital'),
        (IMPRENTA, 'Imprenta'),
        (UNIFORMES, 'Uniformes'),
        (IMAGEN, 'Imagen personal'),
        (DECORACION, 'Decoración'),
        (DISEÑOG, 'Diseño Grafico'),
        (ANUNCIOSP, 'Anuncios Públicos'),
        (FOTOGRAFIA, 'Fotografia'),
        (ESTUDIOSM, 'Estudios de Mercado'),
        (AA, 'Asesoría Aire'),
        #Tierra
        (CONSULTORESPROCESOS, 'Consultores Procesos'),
        (EQCOMPUTO, 'Equipos de Cómputo'),
        (EQCOCINA, 'Equipos de Cocina'),
        (EQELECTRONICOS, 'Equipos Electrónicos'),
        (EQOFICINA, 'Equipos de Oficina'),
        (BIENESRAICES, 'Bienes Raíces'),
        (FERRETERIA, 'Ferretería'),
        (MATERIASPRIMAS, 'Materias primas'),
        (DSOFTWARE, 'Desarrollo de Software'),
        (DISEÑOINDUSTRIAL, 'Diseño Industrial'),
        (INSELECTRECTRICAS, 'Instalaciones Eléctricas'),
        (INSPLUVIALES, 'Instalaciones Pluviales'),
        (MANTENIMIENTO, 'Mantenimiento'),
        (PRODQUIMICOS, 'Productos Quimicos'),
        (ARQUITECTURA, 'Arquitectura'),
        (INGCIVIL, 'Ingeniería Civil'),
        (DISEÑOINTERIORES, 'Diseños de Interiores'),
        (SEGURIDAD, 'Seguridad'),
        (SISTEMASAMIN, 'Sistemas de Amin'),
        (AA, 'Asesoría Tierra'),
        #Agua
        (COAUCHING, 'Coauching'),
        (DH, 'Desarrollo Humano'),
        (EDUCACION, 'Educación'),
        (AP, 'Alianzas politicas'),
        (RESTAURANTES, 'Restaurantes'),
        (BIENESTAR, 'Bienestar'),
        (SALUD, 'Salud'),
        (AAG, 'Asesoria Agua'),
    )

    creado_por = models.ForeignKey(User, default=1, null=True)
    tratamiento = models.CharField(max_length=3, choices=TRATAMIENTOS, default=SEÑOR)
    nombre = models.CharField(max_length=90, default='')
    cargo = models.CharField(max_length=90, default='', blank=True, null=True)
    email = models.EmailField(default='', blank=True, null=True)
    ntd = models.CharField(max_length=2, default=CERO, choices=NIVEL)
    nota = models.TextField(default='', blank=True, null=True)
    fecha_de_creacion = models.DateTimeField(editable=False, auto_now=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    telefono = models.CharField(validators=[phone_regex], max_length=17, blank=True, default='0', null=True)
    extension = models.PositiveSmallIntegerField(blank=True, null=True)
    celular = models.CharField(validators=[phone_regex], max_length=17, blank=True, default='0')
    empresa = models.CharField(max_length=30, default='', blank=True, null=True)
    giro = models.CharField(max_length=4, default='', choices=GIRO)
    subgiro = models.CharField(max_length=30, default='')
    tipo = models.CharField(max_length=3, default=AGUA, choices=ELEMENTO)
    imagen = models.ImageField(blank=True, null=True)

    def __str__(self):
        return '%s' % self.nombre
