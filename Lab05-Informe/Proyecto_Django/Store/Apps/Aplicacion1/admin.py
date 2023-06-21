from django.contrib import admin
from .models import Clasificacion, Cliente, Producto
# Register your models here.
admin.site.register(Clasificacion)
admin.site.register(Cliente)
admin.site.register(Producto)