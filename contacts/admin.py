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


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'giro','tipo','direccion','web',)
    list_editable = ('nombre', 'giro', 'tipo', 'direccion','web',)
    inlines = [
        TelefonoEmpresaInline,
    ]


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'telefono_principal', 'empresa', 'creado_por',)
    list_editable = ('email', 'telefono_principal',)
    list_display_links = ('id', 'nombre', )
    inlines = [
        TelefonoContactoInline,
    ]
