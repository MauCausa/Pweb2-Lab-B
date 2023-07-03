from django.urls import path
#importamos las vistas  de la aplicacion
from . import views

urlpatterns = [
    #
    path('', views.index, name='index'),
]