from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Remera(models.Model):
  articulo = models.CharField(max_length = 50, null = True)
  categoria = models.CharField(max_length = 50, null = True)
  modelo = models.CharField(max_length = 50, null = True)
  talle = models.CharField(max_length = 10, null = True)
  def __str__(self):
    return f"{self.articulo}"

class Pantalon(models.Model):  
  articulo = models.CharField(max_length = 50, null = True)
  categoria = models.CharField(max_length = 50, null = True)
  modelo = models.CharField(max_length = 50, null = True)
  talle = models.IntegerField(null = True)

  def __str__(self):
    return f"{self.articulo}"

class Buzo(models.Model):
  articulo = models.CharField(max_length = 50, null = True)
  categoria = models.CharField(max_length = 50, null = True)
  descripcion = models.CharField(max_length = 100, null = True)
  talle = models.CharField(max_length = 10, null = True)
  def __str__(self):
    return f"{self.articulo}"

class Cliente(models.Model):
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50, null = True)
  def __str__(self):
    return f"{self.nombre}"

class Vendedor(models.Model):
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  edad = models.IntegerField()
  dni = models.CharField(max_length = 20)
  email = models.CharField(max_length=50)
  cuentaDePago = models.CharField(max_length = 50)

  def __str__(self):
    return f"{self.nombre}"


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"