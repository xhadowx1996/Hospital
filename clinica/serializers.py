from rest_framework import serializers
from .models import Consulta, Especialista, Paciente



class PacienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

    
    def create(self, validated_data):
        return Paciente.objects.create(**validated_data)


class ConsultaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

    def create(self, validated_data):
        return Consulta.objects.create(**validated_data)

class EspecialistaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Especialista
        fields = '__all__'

    def create(self, validated_data):
        return Especialista.objects.create(**validated_data)                                   