from django.contrib import admin

from . import models

@admin.register(models.Estadio)
class EstadioAdmin(admin.ModelAdmin):

    list_display = ('pk','nombre', 'ubicacion')
    list_display_links = ('pk', 'nombre')
    search_fields = ('nombre',)


@admin.register(models.LocalidadEvento)
class LocalidadEventoAdmin(admin.ModelAdmin):

    list_display = ('pk','evento', 'localidad', 'aforo', 'precio')
    list_display_links = ('pk', 'evento', 'localidad')
    search_fields = ('estadio', 'localidad', 'aforo')