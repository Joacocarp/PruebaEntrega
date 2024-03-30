from django.db import models
from django.contrib.auth.models import User



class Remera(models.Model):
  articulo = models.CharField(max_length = 50, null = True)
  categoria = models.CharField(max_length = 50, null = True)
  modelo = models.CharField(max_length = 50, null = True)
  talle = models.CharField(max_length = 10, null = True)
  imagenArticulo = models.ImageField(null=True, blank=True, upload_to="imagenes/")
  def __str__(self):
    return f"{self.articulo}"

class Pantalon(models.Model):  
  articulo = models.CharField(max_length = 50, null = True)
  categoria = models.CharField(max_length = 50, null = True)
  modelo = models.CharField(max_length = 50, null = True)
  talle = models.IntegerField(null = True)
  imagenArticulo = models.ImageField(null=True, blank=True, upload_to="imagenes/")

  def __str__(self):
    return f"{self.articulo}"

class Buzo(models.Model):
  articulo = models.CharField(max_length = 50, null = True)
  categoria = models.CharField(max_length = 50, null = True)
  descripcion = models.CharField(max_length = 100, null = True)
  talle = models.CharField(max_length = 10, null = True)
  imagenArticulo = models.ImageField(null=True, blank=True, upload_to="imagenes/")
  def __str__(self):
    return f"{self.articulo}"



class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"