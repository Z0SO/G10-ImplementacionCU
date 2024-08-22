

from django.urls import path, include

# se deben importar el TokenObtainPairView y TokenRefreshView de la libreria rest_framework_simplejwt.views para poder usarlos en las rutas
# cada uno de estos views se encarga de generar un token y de refrescarlo respectivamente
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# se importa el RegisterView que se encarga de registrar un usuario
from .views import RegisterView



urlpatterns = [
   
    # para acceder a la api
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # para refrescar el token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # para registrar un usuario
    path('api/register/', RegisterView.as_view(), name='register'),

]
