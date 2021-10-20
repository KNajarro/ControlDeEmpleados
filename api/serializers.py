from django.db.models import fields
from rest_framework import serializers
from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id', 'tipo_documento', 'documento', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'area', 'subarea')