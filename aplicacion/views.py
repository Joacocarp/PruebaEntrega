from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import * 

from django.views.generic import TemplateView, ListView, DetailView, UpdateView

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class IndexView(TemplateView):
    template_name = 'aplicacion/index.html'

#__Pantalones-View

class PantalonList(ListView):
  model = Pantalon

class PantalonCreate(LoginRequiredMixin, CreateView):
  model = Pantalon
  fields = ["articulo", "categoria", "modelo", "talle", "imagenArticulo"]
  success_url = reverse_lazy("pantalones")

class PantalonUpdate(LoginRequiredMixin, UpdateView):
  model = Pantalon
  fields = ["articulo", "categoria", "modelo", "talle", "imagenArticulo"]
  template_name = 'aplicacion/pantalon_Form.html'
  success_url = reverse_lazy("pantalones")

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class PantalonDelete(LoginRequiredMixin, DeleteView):
    model = Pantalon
    success_url = reverse_lazy("pantalones")  

   


#__Remeras-View

class RemeraList(ListView):
  model = Remera

class RemeraCreate(LoginRequiredMixin, CreateView):
  model = Remera
  fields = ["articulo", "categoria", "modelo", "talle", "imagenArticulo"]
  success_url = reverse_lazy("remeras")

class RemeraUpdate(LoginRequiredMixin, UpdateView):
  model = Remera
  fields = ["articulo", "categoria", "modelo", "talle", "imagenArticulo"]
  template_name = 'aplicacion/remera_Form.html'
  success_url = reverse_lazy("remeras")

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RemeraDelete(LoginRequiredMixin, DeleteView):
    model = Remera
    success_url = reverse_lazy("remeras")  

  


#__Buzos-View

class BuzoList(ListView):
  model = Buzo

class BuzoCreate(LoginRequiredMixin, CreateView):
  model = Buzo
  fields = ["articulo", "categoria", "descripcion", "talle", "imagenArticulo"]
  success_url = reverse_lazy("buzos")

class BuzoUpdate(LoginRequiredMixin, UpdateView):
  model = Buzo
  fields = ["articulo", "categoria", "descripcion", "talle", "imagenArticulo"]
  template_name = 'aplicacion/buzo_Form.html'
  success_url = reverse_lazy("buzos")

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BuzoDelete(LoginRequiredMixin, DeleteView):
    model = Buzo
    success_url = reverse_lazy("buzos")  
  

def clientes(request):
  contexto = {'clientes' : Cliente.objects.all()}
  return render(request, "aplicacion/clientes.html")

def vendedores(request):
  contexto = {'vendedores' : Vendedor.objects.all()}
  return render(request, "aplicacion/vendedores.html")


def acerca(request):
  return render(request, "aplicacion/acerca.html")

def contacto(request):
  return render(request, "aplicacion/contacto.html")

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


#_____forms

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

#______Login/Logout

def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            #______ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm} )

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('index'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm} ) 

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            #___ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #____________________________________________________
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('index'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": miForm} )      

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('index'))
    else:
        # Si la solicitud no es POST, se instancia el formulario con los datos del usuario actual
        miForm = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy("index")
