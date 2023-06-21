from django.db import models

# Create your models here.
class Clasificacion(models.Model):
    tipo = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['tipo']
        
    def __str__(self):
        return self.tipo

class Producto(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre del producto", blank=True)
    descripcion = models.CharField(max_length=300, help_text="Breve descripcion del producto", null=True)
    tipo = models.ManyToManyField(Clasificacion)
    precio = models.FloatField
    cantidad = models.IntegerField
    imagen = models.ImageField(blank=True, null=True)
    class Meta:
        ordering = ['nombre']
        
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    user_name = models.CharField(max_length=255,unique=True ,blank=False, null=True)
    password = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(max_length=255,unique=True, blank=False, null=True)
    class Meta:
        ordering = ['user_name']
    def __str__(self):
        return self.user_name