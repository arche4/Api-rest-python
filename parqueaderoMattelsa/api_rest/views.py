from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from django.shortcuts import get_object_or_404
import base64
from .models import Empleado,Parqueadero,tipoVehiculo
from .serializers import EmpleadoSerializer,ParqueaderoSerializer,tipoVehiculoSerializer



class ListVehiViewSet(viewsets.ModelViewSet):
    model = tipoVehiculo
    serializers_class = tipoVehiculoSerializer
    queryset = tipoVehiculo.objects.all()

class ListCCViewSet(viewsets.ModelViewSet):
    model = Empleado
    serializers_class = EmpleadoSerializer
    queryset = Empleado.objects.all()

class registroIngresoViewSet(viewsets.ModelViewSet):
    model = Parqueadero
    serializers_class = ParqueaderoSerializer
    queryset = Parqueadero.objects.all()

