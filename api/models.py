from django.db import models

# Create your models here.
class Empleado(models.Model):
    tipo_documento = models.CharField(max_length=25)
    documento = models.CharField(max_length=25)
    primer_nombre = models.CharField(max_length=25)
    segundo_nombre = models.CharField(max_length=25)
    primer_apellido = models.CharField(max_length=25)
    segundo_apellido = models.CharField(max_length=25)
    area = models.CharField(max_length=25)
    subarea = models.CharField(max_length=25)

    def __str__(self):
        return self.primer_apellido, self.primer_nombre