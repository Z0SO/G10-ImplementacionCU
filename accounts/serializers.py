
from django.contrib.auth.models import User
from rest_framework import serializers


# Serializador para el modelo User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

        # El password se va a escribir, pero no se va a mostrar
        extra_kwargs = {'password': {'write_only': True}}


    # Sobreescribimos el método create para que el password se guarde encriptado
    def create(self, validated_data):
        
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

        return user
