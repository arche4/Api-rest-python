from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Empleado,Parqueadero,tipoVehiculo


class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id', 'nombreEmp', 'cedulaEmp']
class ParqueaderoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tipoVehiculo
        fields = ['id', 'tipo_vehiculo', 'foto', 'cilindraje', 'placa', 'modelo', 'numPuertas', 'tiempos', 'Empleado_id']
class tipoVehiculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parqueadero
        fields = ['id', 'celda', 'cedulaEmp', 'tipo_vehiculo_id']

