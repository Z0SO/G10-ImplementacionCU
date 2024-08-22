

# serializers.py

from rest_framework import serializers
from .models import Turno, Vehiculo, Mecanico


# serializador para cada modelo


class MecanicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mecanico
        fields = ['id', 'estado', 'especialidad', 'nombre', 'certificacion', 'anios_experiencia']

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['id', 'anio', 'tipo_vehiculo', 'marca', 'modelo', 'matricula', 'utilidad', 'nro_chasis']

class TurnoSerializer(serializers.ModelSerializer):
    vehiculo = VehiculoSerializer()
    mecanico = MecanicoSerializer()

    class Meta:
        model = Turno
        fields = ['id', 'fecha', 'hora', 'vehiculo', 'mecanico']
