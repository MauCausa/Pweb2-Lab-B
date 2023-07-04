from django.db import models

# Create your models here.

class DestinosTuristicos():
    nombreCiudad : str
    descripcionCiudad : str
    imagenCiudad : str
    precioTour : int
    ofertaTour : bool
"""
class DestinosTuristicos(models.Model):
    nombreCuidad = models.CharField(max_length=150, blank=True)
    descripcionCiudad = models.CharField(max_length=400, blank=True)
    imagenCiudad = models.ImageField(blank=True, null=True)
    precioTour = models.FloatField
    ofertaTour = models.BooleanField
"""
"""
???
class Usuario(models.Model):
    nombres = models.CharField(max_length=150, blank=True)
    apellidos = models.CharField(max_length=200, blank=True)
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=50)

"""
