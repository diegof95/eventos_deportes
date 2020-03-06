from django.contrib import admin

from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):

    list_display = ('pk', 'username', 'first_name', 'last_name', 'rol')
    list_display_links = ('pk', 'username')
    search_fields = ('username',)