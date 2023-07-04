from django.shortcuts import render
from .models import DestinosTuristicos
# Create your views here.
def index(request):
    dest1 = DestinosTuristicos()
    dest1.nombreCiudad = "Arequipa"
    dest1.descripcionCiudad = "La ciudad Blanca de Arequipa"
    dest1.imagenCiudad = "destination_01.jpg"
    dest1.precioTour = 800
    dest1.ofertaTour = False
    
    dest2 = DestinosTuristicos()
    dest2.nombreCiudad = "Cusco"
    dest2.descripcionCiudad = "La ciudad Imperial, el Ombligo del Mundo"
    dest2.imagenCiudad = "destination_2.jpg"
    dest2.precioTour = 900
    dest2.ofertaTour = True
    
    dest3 = DestinosTuristicos()
    dest3.nombreCiudad = "Huaraz"
    dest3.descripcionCiudad = "La ciudad Presuncion"
    dest3.imagenCiudad = "destination_3.jpg"
    dest3.precioTour = 700
    dest3.ofertaTour = False
    
    dests = [dest1, dest2, dest3]
    contex = {
        'dests' : dests
    }
    return render(request, 'index.html', contex)