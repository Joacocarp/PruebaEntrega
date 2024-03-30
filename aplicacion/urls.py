from django.urls import path, include
from .views import * 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('acerca/', acerca, name = "acerca_de_mi"),
  
    #__Remeras
    path('pantalones/', PantalonList.as_view(), name = "pantalones"),
    path('pant_create/', PantalonCreate.as_view(), name="pant_create"), 
    path('pant_update/<int:pk>/', PantalonUpdate.as_view(), name="pant_update"), 
    path('pant_delete/<int:pk>/', PantalonDelete.as_view(), name="pant_delete"), 
    #__Pantalones
    path('remeras/', RemeraList.as_view(), name = "remeras"),
    path('reme_create/', RemeraCreate.as_view(), name="reme_create"), 
    path('reme_update/<int:pk>/', RemeraUpdate.as_view(), name="reme_update"), 
    path('reme_delete/<int:pk>/', RemeraDelete.as_view(), name="reme_delete"), 
    
    #__Buzos
    
    path('buzos/', BuzoList.as_view(), name = "buzos"),
    path('buzo_create/', BuzoCreate.as_view(), name="buzo_create"), 
    path('buzo_update/<int:pk>/', BuzoUpdate.as_view(), name="buzo_update"), 
    path('buzo_delete/<int:pk>/', BuzoDelete.as_view(), name="buzo_delete"), 

    #__Login/Logout
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/index.html") , name="logout"),
    path('registro/', register, name="registro"),

     #__Edicion Perfil, Cambio de Clave, Avatar
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

    path('buscar_articulo/', buscar, name = "buscar_articulo"),
    path('encontrar_articulo/', encontrarArticulo, name = "encontrar_articulo"),
    path('cliente_form/', clienteForm, name = "cliente_form"),
    path('clientes/', clientes, name = "clientes"),


]


