from django.contrib.auth.backends import BaseBackend
from sistema.models import Usuario

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            usuario = Usuario.objects.get(email=email)
            if usuario.contrasena == password:  # Aquí reemplaza con hashing si tienes
                return usuario
        except Usuario.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
