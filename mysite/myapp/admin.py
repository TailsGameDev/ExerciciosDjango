from django.contrib import admin
from .models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
    list_display = [
        'usuario', 'senha'
    ]
    search_fields  = ['usuario', 'senha']

admin.site.register(Usuario, UsuarioAdmin)