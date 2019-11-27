from .models import Cliente
from rest_framework import serializers

# un serializers sirve para transformar el objeto
# a json y viceversa, esto para la comunicacion de datos

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'