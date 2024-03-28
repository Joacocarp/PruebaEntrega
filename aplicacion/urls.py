from django.urls import path, include
from .views import * 

urlpatterns = [
    path('', home, name = "home"), 
    #__Remeras
    path('remeras/', remeras, name = "remeras"),
    path('remera_form/', remeraForm, name = "remera_form"),

    #__Pantalones
    path('pantalones/', PantalonList.as_view(), name = "pantalones"),
    path('pant_create/', PantalonCreate.as_view(), name="pant_create"), 
    path('pant_update/<int:pk>/', PantalonUpdate.as_view(), name="pant_update"), 
    path('pant_delete/<int:pk>/', PantalonDelete.as_view(), name="pant_delete"), 
    
    path('buzos/', buzos, name = "buzos"),
    path('clientes/', clientes, name = "clientes"),
    path('acerca/', acerca, name = "acerca_de_mi"),
    path('agregar_cliente/', agregar_cliente, name = "agregar_cliente"),
    path('agregar_remera/', agregar_remera, name = "agregar_remera"),
    
    path('cliente_form/', clienteForm, name = "cliente_form"),
    path('buzo_form/', buzoForm, name = "buzo_form"),

    path('buscar_articulo/', buscar, name = "buscar_articulo"),
    path('encontrar_articulo/', encontrarArticulo, name = "encontrar_articulo"),
]


