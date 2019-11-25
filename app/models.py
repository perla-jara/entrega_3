from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

# Create your models here.


class Pedido(models.Model):
    nombre = models.CharField(max_length=30,null=True)
    fecha = models.DateTimeField(auto_now=True,null=True)
    hora = models.DateTimeField(default=timezone.now,null=True)
    PIZZA = (
        ('SuperPeperonni','SuperPeperonni'),
        ('CarnesMix','CarnesMix'),
        ('Italiana','Italiana'),
        ('Española','Española'),
        ('Napolitana','Napolitana'),
        ('Vegetariana','Vegetariana'),
        ('Hawaiana','Hawaiana'),
    )
    tipo_pizza = models.CharField(max_length=50,choices=PIZZA,null=True)
    TAMAÑO = (
        ('Individual','Individual'),
        ('Mediana','Mediana'),
        ('Grande','Grande'),
        ('XL','XL'),
    )
    tamaño = models.CharField(max_length=50,choices=TAMAÑO,null=True)
    CANTIDAD_PIZZA = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
    )
    cantidad_pizza = models.CharField(max_length=50,choices=CANTIDAD_PIZZA,null=True)
    ACOMPAÑAMIENTO = (
        ('PalitosQueso','PalitosQueso'),
        ('PalitosAjo','PalitosAjo'),
        ('PalitosCanela','PalitosCanela'),
    )
    acompañamiento = models.CharField(max_length=50,choices=ACOMPAÑAMIENTO,null=True)
    CANTIDAD_ACOMPAÑAMIENTO = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
    )
    cantidad_acompañamiento = models.CharField(max_length=50,choices=CANTIDAD_ACOMPAÑAMIENTO,null=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        permissions = (
        ('administrador',_('Es administrador')),
        ('cliente',_('Es cliente')),
    )

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    celular = models.CharField(max_length=12)
    contraseña = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
        
    class Meta:
        permissions = (
            ('administrador',_('Es administrador')),
            ('cliente',_('Es cliente')),
        )


