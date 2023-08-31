from django.db import models

# Create your models here.

class Oficina(models.Model):
    codigOficina = models.IntegerField()
    nombreOficina = models.CharField(max_length=50)
    liderOficina = models.CharField(max_length=30)

class Cita(models.Model):
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    identificacion = models.CharField(max_length=20)
    nombre_completo = models.CharField(max_length=200)
    correo_electronico = models.EmailField()