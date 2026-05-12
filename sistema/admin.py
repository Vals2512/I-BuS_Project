from django.contrib import admin
from .models import *

# Registro normal de modelos para CRUD completo
admin.site.register(Barrio)
admin.site.register(Empresa)
admin.site.register(Tiempo)
admin.site.register(Horario)
admin.site.register(TipoUsuario)
admin.site.register(Ruta)
admin.site.register(RutaBarrio)
admin.site.register(DetalleRuta)

# Registro del modelo Usuario con restricciones
from django.contrib.admin import ModelAdmin

class UsuarioReadOnlyAdmin(ModelAdmin):
    readonly_fields = ["email", "idTipoUsuario"]
    list_display = ["idUsuario", "email", "idTipoUsuario"]
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Usuario, UsuarioReadOnlyAdmin)
