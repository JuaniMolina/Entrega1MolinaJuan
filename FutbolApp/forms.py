from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=50, label='nombre')
    apellido = forms.CharField(max_length=50, label='apellido')
    fechaNacimiento = forms.DateField(label='fechaNacimiento')
    nacionalidad = forms.CharField(max_length=30, label='nacionalidad')
    tamanio = forms.IntegerField(label='tamanio')
    peso = forms.IntegerField(label='peso')

class PaisForm(forms.Form):
    nombre = forms.CharField(max_length=30, label='nombre')
    colores = forms.CharField(max_length=30, label='colores')
    diminutivo = forms.CharField(max_length=10, label='diminutivo')

class ClubFutbolForm(forms.Form):
    pais = forms.CharField(max_length=30, label='pais')
    nombre = forms.CharField(max_length=30, label='nombre')
    apodo = forms.CharField(max_length=30, label='apodo')
    colores = forms.CharField(max_length=30, label='colores')
    fundacion = forms.CharField(max_length=30, label='fundacion')
    web = forms.URLField(label='web')
    diminutivo = forms.CharField(max_length=10, label='diminutivo')