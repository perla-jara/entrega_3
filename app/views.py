from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from datetime import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Correos
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
#---
from .models import Cliente

from .forms import ClienteForm, RestablecerForm

# API
from rest_framework import generics
from .serializers import ClienteSerializers


class API_objects(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers


class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers



def login(request):
    return render(request, 'app/login.html', {})


def cliente_list(request):
    user = request.user
    if user.has_perm('app.administrador'):
        clientes = Cliente.objects.filter(
            published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'app/listar_clientes.html', {'clientes': clientes})
    else:
        return render(request, 'app/menu.html')


def menu(request):
    return render(request, 'app/menu.html', {})


def ingresar(request):
    return render(request, 'app/login.html', {})


def locales(request):
    return render(request, 'app/locales.html', {})


def quienes_somos(request):
    return render(request, 'app/quienes_somos.html', {})


def listar_clientes(request):
    clientes = Cliente.objects.filter(nombre__contains='')
    return render(request, "app/listar_clientes.html", {'clientes': clientes})


def editar_cliente(request, cliente_id):
    instancia = Cliente.objects.get(id=cliente_id)
    form = ClienteForm(instance=instancia)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request, "app/editar_cliente.html", {'form': form})


def borrar_cliente(request, cliente_id):
    instacia = Cliente.objects.get(id=cliente_id)
    instacia.delete()
    return redirect('/listar_clientes')


class Cliente_Create(CreateView):
    model = Cliente
    form_class = ClienteForm
    templates_name = 'app/agregar_cliente.html'
    success_url = reverse_lazy('cliente_crear')

# Recuperacion Contraseña


def olvido(request):
    form = RestablecerForm(request.POST or None)
    mensaje = ""
    if form.is_valid():
        data = form.cleaned_data
        user = User.objects.get(username=data.get("username"))
        send_mail(
            'Recuperación de contraseña',
            'Haga click aquí para ingresar una nueva contraseña',
            'a.duoc@gmail.com',
            [user.email],
            html_message='Pulse <a href="http://localhost:8000/restablecer?user=' +
            user.username+'">aquí</a> para restablecer su contraseña.',
        )
        mensaje = 'Correo Enviado a '+user.email
    return render(request, "app/pasword/olvido.html", {'form': form, 'mensaje': mensaje, 'titulo': "Recuperar Contraseña", })

# Restablecer Contraseña


def restablecer(request):
    form = RestablecerForm(request.POST or None)
    mensaje = ""
    try:
        username = request.GET["user"]
    except Exception as e:
        username = None
    if username is not None:
        if form.is_valid():
            data = form.cleaned_data
            if data.get("password_A") == data.get("password_B"):
                mensaje = "La contraseña se ha restablecido"
                contra = make_password(data.get("password_B"))
                User.objects.filter(username=username).update(password=contra)
            else:
                mensaje = "Las contraseñas no coinciden"
        return render(request, "app/pasword/restablecer.html", {'form': form, 'username': username, 'mensaje': mensaje, 'titulo': "Restablecer Contraseña", })
    else:
        return redirect('/login/')
