from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users', blank=True, null=True)
    numero = models.CharField(max_length=12, default='', help_text='Ingresa un numero no mayor a 12 digitos')
    miembro_desde = models.DateTimeField(editable=False, auto_now=True)
    cargo = models.CharField(max_length=28, default='', blank=True, null=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
