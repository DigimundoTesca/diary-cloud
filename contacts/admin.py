from django.contrib import admin
from .models import Contacto, Telefono


class TelefonoAdmin(admin.TabularInline):
    model = Telefono
    extra = 0


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'empresa', 'telefono', 'nota')
    inlines = (TelefonoAdmin, )
