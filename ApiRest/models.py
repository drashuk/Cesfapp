from django.db import models
from django.core.validators import MinLengthValidator

class Medicamento(models.Model):
    id_medicamento = models.IntegerField(primary_key=True, blank=True)
    nombre = models.CharField(max_length=50, blank=True)
    dosis = models.CharField(max_length=50, blank=True)
    stock = models.IntegerField(blank=True)
    def __str__(self):
        return  self.nombre + " - " + self.dosis

class Ficha(models.Model):
    id_ficha = models.IntegerField(primary_key=True)
    rut = models.CharField(max_length=10, blank=False, validators=[MinLengthValidator(8)])
    nombre = models.CharField(max_length=50)
    diagnostico = models.CharField(max_length=500)
    def __str__(self):
        return self.nombre

class Prescripcion(models.Model):
    id_prescripcion = models.IntegerField(primary_key=True)
    ficha = models.ForeignKey(Ficha, on_delete=models.CASCADE, related_name='medicamentos')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, related_name='prescripciones')
    frecuencia = models.CharField(max_length=50, default='', blank=False)
    entregado = models.BooleanField(default=False)
    def __str__(self):
        return self.ficha.nombre + " - " + self.medicamento.nombre
