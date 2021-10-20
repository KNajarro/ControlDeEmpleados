from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmpleadoSerializer
from .models import Empleado

# Create your views here.
class EmpleadoViewSet(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()