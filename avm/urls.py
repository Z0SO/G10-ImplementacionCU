# avm/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TurnoViewSet, VehiculoViewSet, MecanicoViewSet

# se define el enrutador
router = DefaultRouter()

# se registran las rutas para cada modelo
router.register(r'turnos', TurnoViewSet)
router.register(r'vehiculos', VehiculoViewSet)
router.register(r'mecanicos', MecanicoViewSet)

# se definen las rutas

urlpatterns = [
    path('', include(router.urls)),
]
