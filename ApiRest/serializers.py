from rest_framework import serializers
from .models import *

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class PrescripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescripcion
        fields = '__all__'

class PrescripcionDetalleSerializer(serializers.ModelSerializer):
    nombre = serializers.ReadOnlyField(source='medicamento.nombre')
    dosis = serializers.ReadOnlyField(source='medicamento.dosis')
    class Meta:
        model = Prescripcion
        fields = ['nombre','dosis','frecuencia', 'entregado']

class FichaSerializer(serializers.ModelSerializer):
    medicamentos = PrescripcionDetalleSerializer(many=True, read_only=True)
    class Meta:
        model = Ficha
        fields = ['id_ficha','nombre','rut','diagnostico', 'medicamentos']