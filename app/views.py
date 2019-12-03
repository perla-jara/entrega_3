from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# -----------  para nuestos modelos --------------------
from .models import Cliente
from .forms import ClienteForm
# API
from rest_framework import generics 
from .serializers import ClienteSerializers

class API_objects(generics.ListCreateAPIView):
        queryset= Cliente.objects.all()
        serializer_class= ClienteSerializers

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
        queryset= Cliente.objects.all()
        serializer_class= ClienteSerializers


def login(request):
    return render(request, 'app/login.html', {})

def cliente_list(request):
    user = request.user
    if user.has_perm('app.administrador'):
        clientes = Cliente.objects.filter(
            published_date__lte=timezone.now()).order_by('published_date')
        return render(request,'app/listar_clientes.html', {'clientes': clientes})
    else:
        return render(request,'app/menu.html')
        
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
    instancia= Cliente.objects.get(id=cliente_id)
    form=  ClienteForm(instance=instancia)
    if request.method=="POST":
        form= ClienteForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia= form.save(commit=False)
            instancia.save()
    return render(request, "app/editar_cliente.html",{'form':form})            

def borrar_cliente(request, cliente_id):    
    instacia= Cliente.objects.get(id=cliente_id)
    instacia.delete()
    return redirect('/listar_clientes')

class Cliente_Create(CreateView):
    model = Cliente
    form_class = ClienteForm
    templates_name = 'app/agregar_cliente.html'
    success_url = reverse_lazy('cliente_crear')

