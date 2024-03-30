from django import forms 
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
class ClienteForm(forms.Form):
  nombre = forms.CharField(max_length = 50, required = True)
  apellido = forms.CharField(max_length = 50, required = True)
  
class RemeraForm(forms.Form):
  articulo = forms.CharField(max_length = 50, required = True)
  categoria = forms.CharField(max_length = 50, required = True)
  modelo = forms.CharField(max_length = 50, required = False)
  talle = forms.CharField(max_length = 10, required = True)



class BuzoForm(forms.Form):
  articulo = forms.CharField(max_length = 50, required = True)
  categoria = forms.CharField(max_length = 50, required = True)
  descripcion = forms.CharField(max_length = 100, required = False)
  talle = forms.IntegerField(required = True)


class RegistroForm(UserCreationForm): 
    email = forms.EmailField(required=True)   
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserEditForm(UserChangeForm): 
    email = forms.EmailField(required=True)   
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]    

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
       return f"{self.user} - {self.imagen}"

