from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import * 


from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def home(request):
  return render(request, "aplicacion/index.html")

def remeras(request):
  contexto = {'remeras': Remera.objects.all()}
  return render(request, "aplicacion/remeras.html")

#__Pantalones

class PantalonList(ListView):
  model = Pantalon

class PantalonCreate(CreateView):
    model = Pantalon
    fields = ["articulo", "categoria", "modelo", "talle"]
    success_url = reverse_lazy("pantalones")

class PantalonUpdate(UpdateView):
    model = Pantalon
    fields = ["articulo", "categoria", "modelo", "talle"]
    success_url = reverse_lazy("pantalones")


class PantalonDelete(DeleteView):
    model = Pantalon
    success_url = reverse_lazy("pantalones")  
  

def buzos(request):
  contexto = {'buzos': Buzo.objects.all()}
  return render(request, "aplicacion/buzos.html")

def clientes(request):
  contexto = {'clientes' : Cliente.objects.all()}
  return render(request, "aplicacion/clientes.html")

def vendedores(request):
  contexto = {'vendedores' : Vendedor.objects.all()}
  return render(request, "aplicacion/vendedores.html")


def acerca(request):
  return render(request, "aplicacion/acerca.html")

def agregar_cliente(request):
  cliente = Cliente(nombre = "Joaco", apellido = "Gonzalez")
  cliente.save()
  respuesta = f"<html><h1>Se guardo el cliente</h1> </html>"
  return HttpResponse(respuesta)

def agregar_vendedor(request):
  vendedor = Vendedor(nombre = "Empresario")
  vendedor.save()
  respuesta = f"<html><h1>Se guardo el vendedor</h1> </html>"
  return HttpResponse(respuesta)


def agregar_remera(request):
  remera = Remera(articulo = "articulo", categoria = "categoria", modelo = "modelo", talle = "talle")
  remera.save()
  respuesta = f"<html><h1>Se guardo el articulo</h1> </html>"
  return HttpResponse(respuesta)

#______________forms

def clienteForm(request):
  if request.method == "POST":
    miForm = ClienteForm(request.POST)
    if miForm.is_valid():
      cliente_nombre = miForm.cleaned_data.get("nombre")
      cliente_apellido = miForm.cleaned_data.get("apellido")
      cliente = Cliente(nombre = cliente_nombre, apellido = cliente_apellido)
      cliente.save()
      return render(request, "aplicacion/index.html")
  else:
    miForm = ClienteForm()
    
  return render(request, "aplicacion/clienteForm.html", {"form": miForm})


def remeraForm(request):
  if request.method == "POST":
    miForm = RemeraForm(request.POST)
    if miForm.is_valid():
      remera_nombre = miForm.cleaned_data.get("articulo")
      remera_categoria = miForm.cleaned_data.get("categoria")
      remera_modelo = miForm.cleaned_data.get("modelo")
      remera_talle = miForm.cleaned_data.get("talle")
      remera = Remera(articulo = remera_nombre,  categoria = remera_categoria, modelo = remera_modelo, talle = remera_talle)
      remera.save()
      return render(request, "aplicacion/index.html")
  else:
    miForm = RemeraForm()
    
  return render(request, "aplicacion/remeraForm.html", {"form": miForm})


def buzoForm(request):
  if request.method == "POST":
    miForm = BuzoForm(request.POST)
    if miForm.is_valid():
      buzo_nombre = miForm.cleaned_data.get("articulo")
      buzo_categoria = miForm.cleaned_data.get("categoria")
      buzo_descripcion = miForm.cleaned_data.get("descripcion")
      buzo_talle = miForm.cleaned_data.get("talle")
      buzo = Buzo(articulo = buzo_nombre,  categoria = buzo_categoria, descripcion = buzo_descripcion, talle = buzo_talle)
      buzo.save()
      return render(request, "aplicacion/index.html")
  else:
    miForm = BuzoForm()
    
  return render(request, "aplicacion/buzoForm.html", {"form": miForm})



def buscar(request):
  return render(request, "aplicacion/buscar.html")


def encontrarArticulo(request):
  if request.GET["buscar"]:
    patron = request.GET["buscar"]
    remera = Remera.objects.filter(articulo__icontains = patron)
    contexto = {"remeras": remera}
    return render(request, "aplicacion/remeras.html", contexto)
  
  contexto = {"remeras": Remera.objects.all()}
  return render(request, "aplicacion/buscar.html")