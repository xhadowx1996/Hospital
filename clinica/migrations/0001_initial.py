# Generated by Django 3.2.7 on 2021-09-13 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('CancidadPasientes', models.CharField(max_length=20)),
                ('NombreEspecialista', models.CharField(max_length=25)),
                ('TipoConsulta', models.CharField(max_length=100)),
                ('EstadoConsulta', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'consulta',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Edad', models.CharField(max_length=100)),
                ('Peso', models.CharField(max_length=100)),
                ('Estatura', models.CharField(max_length=100)),
                ('Descripcion', models.CharField(max_length=100)),
                ('Prioridad', models.BooleanField(default=False)),
                ('Fuma', models.BooleanField(default=False)),
                ('Dieta', models.BooleanField(default=False)),
                ('HistoriaClinicas', models.CharField(max_length=100)),
                ('PacienteConsultas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinica.consulta')),
            ],
            options={
                'db_table': 'paciente',
            },
        ),
        migrations.CreateModel(
            name='Especialista',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Medico', models.CharField(max_length=100)),
                ('Especilidad', models.CharField(max_length=100)),
                ('Consultas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinica.consulta')),
            ],
            options={
                'db_table': 'especialista',
            },
        ),
    ]
