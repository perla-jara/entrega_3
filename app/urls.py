from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('agregar_cliente', views.Cliente_Create.as_view(), name="cliente_crear"),
    path('listar_clientes',views.listar_clientes),
    path('editar_cliente/<int:cliente_id>', views.editar_cliente),
    path('borrar_cliente/<int:cliente_id>', views.borrar_cliente),
    path('menu',views.menu),
    path('',views.menu),
    path('locales',views.locales),
    path('quienes_somos',views.quienes_somos),
]
