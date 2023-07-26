from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length= 50)
    password = models.CharField(max_length= 20)
    email = models.EmailField
    nombres = models.CharField(max_length= 200)
    apellidos = models.CharField(max_length= 150)
    isPremium = models.BooleanField(default=False)

class Bodega(models.Model):
    Customer_Name = models.CharField(max_length=100)
    Product = models.CharField(max_length=50)
    Price =  models.PositiveSmallIntegerField()
    is_activate = models.BooleanField(default=True)
