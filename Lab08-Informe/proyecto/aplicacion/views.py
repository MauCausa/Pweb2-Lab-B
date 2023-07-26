from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .serializers import UsuarioSerializer
from .models import Usuario


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
def register(request):
    if request.method == 'POST':
        serializer = UsuarioSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('login')
    else:
        serializer = UsuarioSerializer()

    return render(request, 'register.html', {'serializer': serializer})

def login_view(request):
    if request.method == 'POST':
        passw = request.POST.get('password')
    try:
        user = Usuario.objects.get(username = request.POST.get('username'))
        usname = request.POST.get('username')
        if user.password == passw:
            serializer = UsuarioSerializer(user)
            print("singup")
            request.session['username'] = usname
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Credenciales inválidas'})
        print("credencial invalida")
    except Usuario.DoesNotExist:
        return render(request, 'login.html', {'error_message': 'Credenciales inválidas'})
        print("credencial invalida x2")

    return Response({'error': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

def home(request):
    username = request.session.get('username')
    print("redirigiendo a home")
    return render(request, 'home.html', {'username':username})
