
# importamos User de models
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import AllowAny
from accounts.serializers import UserSerializer

# la vista registerView utiliza el serializador UserSerializer y el modelo User
# ademas de que se le asigna el permiso de AllowAny para que cualquier usuario pueda registrarse

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
