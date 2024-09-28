from django.contrib import admin
from .models import Recurso

@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'propietario')  # Muestra estos campos en la lista
    search_fields = ('nombre',)  # Permite buscar por nombre
