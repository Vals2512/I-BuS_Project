
from datetime import date
from django import forms
from .models import Barrio, DetalleRuta, Empresa, Ruta, Horario, RutaBarrio, Tiempo, Usuario
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class LoginForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico")
    contrasena = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

    def clean_anioFundacion(self):
        anio = self.cleaned_data['anioFundacion']
        anio_actual = date.today().year
        if anio < 0:
            raise forms.ValidationError("El año de fundación no puede ser negativo.")
        if anio > anio_actual:
            raise forms.ValidationError("El año de fundación no puede ser mayor al actual.")
        return anio

    def clean_cantBuses(self):
        cant = self.cleaned_data['cantBuses']
        if cant < 0:
            raise forms.ValidationError("La cantidad de buses no puede ser negativa.")
        return cant

    def clean_cantConductores(self):
        cant = self.cleaned_data['cantConductores']
        if cant < 0:
            raise forms.ValidationError("La cantidad de conductores no puede ser negativa.")
        return cant
    



class RutaForm(forms.ModelForm):
    barrios = forms.ModelMultipleChoiceField(
        queryset=Barrio.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Barrios por los que pasa la ruta"
    )

    class Meta:
        model = Ruta
        fields = ['idEmpresa', 'inicioRuta', 'destinoRuta', 'frecuencia', 'barrios']

    def save(self, commit=True):
        ruta = super().save(commit=commit)

    # Si la ruta ya tiene un ID (ya fue guardada)
        if ruta.pk:
        # Barrios seleccionados manualmente
            barrios_seleccionados = list(self.cleaned_data.get('barrios', []))

        # Agregar inicio y destino si no están incluidos
            if ruta.inicioRuta not in barrios_seleccionados:
                barrios_seleccionados.append(ruta.inicioRuta)

            if ruta.destinoRuta not in barrios_seleccionados:
                barrios_seleccionados.append(ruta.destinoRuta)

        # Eliminar relaciones anteriores
        from .models import RutaBarrio
        RutaBarrio.objects.filter(idRuta=ruta).delete()

        # Crear nuevas relaciones
        for barrio in barrios_seleccionados:
            RutaBarrio.objects.create(idRuta=ruta, idBarrio=barrio)

        return ruta



class RegistroUsuarioForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico')
    contrasena = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    confirmar_contrasena = forms.CharField(widget=forms.PasswordInput, label='Confirmar contraseña')

    def clean(self):
        cleaned_data = super().clean()
        contrasena = cleaned_data.get('contrasena')
        confirmar_contrasena = cleaned_data.get('confirmar_contrasena')

        if contrasena != confirmar_contrasena:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['idEmpresa', 'horaSalida', 'horaLlegada']
        labels = {
            'idEmpresa': 'Empresa',
            'horaSalida': 'Hora de Salida',
            'horaLlegada': 'Hora de Llegada',
        }
        widgets = {
            'horaSalida': forms.TimeInput(attrs={'type': 'time'}),
            'horaLlegada': forms.TimeInput(attrs={'type': 'time'}),
        }


class TiempoForm(forms.ModelForm):
    class Meta:
        model = Tiempo
        fields = ['fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class DetalleRutaForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
        }),
        label="Fecha"
    )
    
    class Meta:
        model = DetalleRuta
        fields = ['idRuta', 'cantidadPasajeros']
        widgets = {
            'idRuta': forms.Select(attrs={'class': 'form-select'}),
            'cantidadPasajeros': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }

    def clean_cantidadPasajeros(self):
        pasajeros = self.cleaned_data.get('cantidadPasajeros')
        if pasajeros is None or pasajeros < 0:
            raise ValidationError("La cantidad de pasajeros debe ser un número positivo.")
        return pasajeros

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha > date.today():
            raise ValidationError("La fecha no puede ser futura.")
        return fecha
    

class BarrioForm(forms.ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombreBarrio']
        labels = {
            'nombreBarrio': 'Nombre del Barrio',
        }

class BusquedaBarriosForm(forms.Form):
    barrio = forms.CharField(
        required=False,
        label='Buscar barrio',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe un barrio...'})
    )

    barrios = forms.ModelMultipleChoiceField(
        required=False,
        label='Seleccionar barrios',
        queryset=Barrio.objects.none(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'scroll-barrios'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['barrios'].queryset = Barrio.objects.all()

class ActualizarCuentaForm(forms.ModelForm):
    contrasena = forms.CharField(
        label='Contraseña', 
        widget=forms.PasswordInput(render_value=True), 
        required=False,
        help_text='Dejar vacío para no cambiar la contraseña'
    )

    class Meta:
        model = Usuario
        fields = ['email', 'contrasena']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Usuario.objects.filter(email=email).exclude(idUsuario=self.instance.idUsuario).exists():
            raise forms.ValidationError('Este correo ya está en uso.')
        return email

    def save(self, commit=True):
        usuario = super().save(commit=False)
        contrasena = self.cleaned_data.get('contrasena')
        if contrasena:
            # Guardar la contraseña tal cual, sin hashear
            usuario.contrasena = contrasena
        else:
            # Mantener la contraseña anterior si no cambió
            usuario.contrasena = self.instance.contrasena
        
        if commit:
            usuario.save()
        return usuario
