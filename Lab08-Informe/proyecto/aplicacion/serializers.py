from rest_framework import serializers
from .models import Usuario
from .models import Bodega

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'password', 'email','nombres', 'apellidos', 'isPremium')
        
    def create(self, validated_data):
        user = Usuario(**validated_data)
        user.save()
        return user
        
class BodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodega
        #fields = ('fullname', 'nickname')
        fields = '__all__'
