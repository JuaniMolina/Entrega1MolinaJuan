from django.db import models

# Create your models here.

class Persona (models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fechaNacimiento=models.DateField()
    nacionalidad=models.CharField(max_length=30)
    tamanio=models.IntegerField()
    peso=models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'

class Pais (models.Model):
    nombre=models.CharField(max_length=30)
    colores=models.CharField(max_length=30)
    diminutivo=models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.diminutivo} - {self.nombre}'

class ClubFutbol(models.Model):
    pais=models.CharField(max_length=30)
    nombre=models.CharField(max_length=30)
    apodo=models.CharField(max_length=30)
    colores=models.CharField(max_length=30)
    fundacion=models.CharField(max_length=30)
    web=models.URLField()
    diminutivo=models.CharField(max_length=10)

    def __str__(self):
        return f'{self.diminutivo} - {self.nombre}'


