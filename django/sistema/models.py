from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class TipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(primary_key=True)
    nombreTipo = models.CharField(max_length=50)

    class Meta:
        db_table = 'TipoUsuario'

    def __str__(self):
        return self.nombreTipo


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    idTipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    email = models.CharField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=100)

    class Meta:
        db_table = 'Usuario'

    def __str__(self):
        return self.email


class Empresa(models.Model):
    idEmpresa = models.AutoField(primary_key=True)
    nombreEmpresa = models.CharField(max_length=100)
    anioFundacion = models.IntegerField()
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    cantBuses = models.IntegerField()
    cantConductores = models.IntegerField()

    class Meta:
        db_table = 'Empresa'

    def __str__(self):
        return self.nombreEmpresa

class Barrio(models.Model):
    idBarrio = models.AutoField(primary_key=True)
    nombreBarrio = models.CharField(max_length=100)

    class Meta:
        db_table = 'Barrio'

    def __str__(self):
        return self.nombreBarrio


class Ruta(models.Model):
    idRuta = models.AutoField(primary_key=True)
    idEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    inicioRuta = models.ForeignKey(Barrio, related_name='ruta_inicio', on_delete=models.CASCADE)
    destinoRuta = models.ForeignKey(Barrio, related_name='ruta_destino', on_delete=models.CASCADE)
    frecuencia = models.CharField(max_length=50)

    class Meta:
        db_table = 'Ruta'

    @property
    def get_barrios(self):
        return Barrio.objects.filter(rutabarrio__idRuta=self)

    def __str__(self):
        return f"{self.inicioRuta.nombreBarrio} - {self.destinoRuta.nombreBarrio}"




class Horario(models.Model):
    idHorario = models.AutoField(primary_key=True)
    idEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    horaSalida = models.TimeField()
    horaLlegada = models.TimeField()

    class Meta:
        db_table = 'Horario'

    def __str__(self):
        return f"Horario Empresa {self.idEmpresa} - {self.horaSalida} a {self.horaLlegada}"


def validate_fecha_pasada(value):
    if value > timezone.now().date():
        raise ValidationError('No se puede ingresar una fecha futura.')
    
class Tiempo(models.Model):
    idTiempo = models.AutoField(primary_key=True)
    fecha = models.DateField(validators=[validate_fecha_pasada])

    class Meta:
        db_table = 'Tiempo'

    @property
    def diaSemana(self):
        return self.fecha.strftime('%A')

    @property
    def numeroSemana(self):
        return self.fecha.isocalendar()[1]

    @property
    def mes(self):
        return self.fecha.strftime('%B')

    def __str__(self):
        return f"{self.fecha} ({self.diaSemana}, Semana {self.numeroSemana}, {self.mes})"
   
class DetalleRuta(models.Model):
    idDetalleRuta = models.AutoField(primary_key=True)
    idRuta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    idTiempo = models.ForeignKey(Tiempo, on_delete=models.CASCADE)
    cantidadPasajeros = models.IntegerField()

    class Meta:
        db_table = 'DetalleRuta'

    def __str__(self):
        return f"Ruta {self.idRuta} - Tiempo {self.idTiempo} - Pasajeros {self.cantidadPasajeros}"

class RutaBarrio(models.Model):
    idRutaBarrio = models.AutoField(primary_key=True)
    idRuta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    idBarrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)

    class Meta:
        db_table = 'RutaBarrio'

    def __str__(self):
        return f"Ruta {self.idRuta} - Barrio {self.idBarrio}"
