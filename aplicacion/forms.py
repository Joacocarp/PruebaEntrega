from django import forms 

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