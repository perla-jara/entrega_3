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

