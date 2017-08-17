from django.contrib import admin
from .models import Contacto, Telefono, Empresa


class TelefonoAdmin(admin.TabularInline):
    model = Telefono
    extra = 0

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
        list_display = ('id', 'nombre', 'giro','tipo','direccion','web')


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'telefono_principal', 'empresa', 'usuario',)
    list_editable = ('email', 'telefono_principal', 'empresa', 'usuario',)
    list_display_links = ('id', 'nombre', )
    inlines = (TelefonoAdmin, )
