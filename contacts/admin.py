from django.contrib import admin
from .models import Contacto, Empresa

from phones.models import TelefonoEmpresa
from phones.models import TelefonoContacto


class TelefonoContactoInline(admin.TabularInline):
    model = TelefonoContacto
    extra = 2


class TelefonoEmpresaInline(admin.TabularInline):
    model = TelefonoEmpresa
    extra = 2


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'creado_por',)
    list_editable = ('email',)
    list_display_links = ('id', 'nombre', )

