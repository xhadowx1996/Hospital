from django.db import models


class Consulta(models.Model):
    id = models.AutoField(primary_key=True)
    CancidadPasientes = models.CharField(max_length=20)
    NombreEspecialista = models.CharField(max_length=25)
    TipoConsulta = models.CharField(max_length=100)
    EstadoConsulta = models.CharField(max_length=100)
    class Meta:
        db_table = 'consulta'

class Especialista(models.Model):
    id = models.AutoField(primary_key=True)
    Medico = models.CharField(max_length=100)
    Especilidad = models.CharField(max_length=100)
    Consultas = models.ForeignKey(Consulta,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = 'especialista'


class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Edad = models.CharField(max_length=100,null=False)
    Peso = models.CharField(max_length=100)
    Estatura = models.CharField(max_length=100,null=False)
    Descripcion = models.CharField(max_length=100)
    Prioridad = models.BooleanField(default=False)
    Fuma = models.BooleanField(default=False)
    Dieta = models.BooleanField(default=False)
    HistoriaClinicas = models.CharField(max_length=100)
    PacienteConsultas = models.ForeignKey(Consulta,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = 'paciente'