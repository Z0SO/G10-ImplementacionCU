

from rest_framework import viewsets
from .models import Turno, Vehiculo, Mecanico
from .serializers import TurnoSerializer, VehiculoSerializer, MecanicoSerializer

# ademas se debe importar el permiso que se va a utilizar en este caso IsAuthenticated
from rest_framework.permissions import IsAuthenticated




class MecanicoViewSet(viewsets.ModelViewSet):
    
    # aqui se define la consulta a la base de datos, en este caso se obtienen todos los registros
    queryset = Mecanico.objects.all()

    # aqui se define el serializador que se usara para convertir los datos de la base de datos en JSON
    serializer_class = MecanicoSerializer
    permission_classes = [IsAuthenticated]  # se define el permiso que se requiere para acceder a esta vista



# se hace lo mismo para los otros dos modelos
class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [IsAuthenticated] 

class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer
    permission_classes = [IsAuthenticated] 
