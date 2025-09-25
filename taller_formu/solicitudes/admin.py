from django.contrib import admin
from .models import Solicitud

@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'documento', 'correo', 'telefono', 'tipo', 'asunto', 'fecha', 'creado_en')
    list_filter = ('tipo', 'fecha')
    search_fields = ('nombre', 'documento', 'correo', 'asunto')
