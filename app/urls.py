from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login_required
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import login


urlpatterns = [
    path('api/', views.API_objects.as_view()),
    path('api/<int:pk>/', views.API_objects_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('agregar_cliente', views.Cliente_Create.as_view(), name="cliente_crear"),
    path('listar_clientes', views.listar_clientes),
    path('editar_cliente/<int:cliente_id>', views.editar_cliente),
    path('borrar_cliente/<int:cliente_id>', views.borrar_cliente),
    path('menu', views.menu),
    path('', views.menu),
    path('login', views.login),
    path('locales', views.locales),
    path('quienes_somos', views.quienes_somos),
    url(r'^$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^olvido/$', views.olvido),
    url(r'^restablecer/$', views.restablecer),
]
