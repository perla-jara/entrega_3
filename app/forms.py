from django import forms
from .models import *
class ClienteForm(forms.ModelForm):
    attrs = {
        "type": "password"
    }
    contraseña = forms.CharField(widget=forms.TextInput(attrs=attrs))

    class Meta:
        model= Cliente
        fields= ['nombre', 'rut', 'email', 'celular', 'contraseña']

# Formulario para Email Restablece Contraseña


class RecuperacionForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(), label="Nombre de Usuario")

# Formulario para Restablecer Contraseña


class RestablecerForm(forms.Form):
    password_A = forms.CharField(
        widget=forms.PasswordInput(), label="Nueva Contraseña")
    password_B = forms.CharField(
        widget=forms.PasswordInput(), label="Repita Contraseña")
