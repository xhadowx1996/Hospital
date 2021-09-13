import os
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import  PacienteSerializers, ConsultaSerializers,EspecialistaSerializers
from .models import  Consulta, Especialista, Paciente
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response


class PacienteView(APIView):
    def get(self, request):
        if request.method == 'GET':
            Pacuiente = Paciente.objects.filter(Prioridad = True)
            print(Pacuiente)
            serializer = PacienteSerializers(Pacuiente, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
       

    def post (self,request):
        if request.method == 'POST':
            serializer = PacienteSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'error': False,
                    'message': "Paciente Clinico Creada Con Exito",
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'error': True,
                    'message': "Invalid form",
                }, status=status.HTTP_400_BAD_REQUEST)

                 
class PcienteFumador(APIView):
    def get(self, request):
        if request.method == 'GET':
            Pacientefumador = Paciente.objects.filter(Fuma = True)
            print(Pacientefumador)
            serializer = PacienteSerializers(Pacientefumador, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'error': False,
                    'message': "el paciente debe ingresar por urgencias",
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'error': True,
                    'message': "Invalid form",
                }, status=status.HTTP_400_BAD_REQUEST)

class PacienteViejo(APIView):
    def get(self,request):
        if request.method == 'GET':
            PacienteAn = Paciente.objects.filter(Edad = True)
            serializer = PacienteSerializers(PacienteAn, many=True)
            Mayores = []
            for a in PacienteAn:
                if a < 40:
                    Mayores.push(a)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({
                            'error': False,
                            'message': "cucho",
                        }, status=status.HTTP_201_CREATED)
                    else:
                        return Response({
                            'error': True,
                            'message': "Invalid form",
                        }, status=status.HTTP_400_BAD_REQUEST)



class ConsultaView(APIView):
    def post (self,request):
        if request.method == 'POST':
            serializer = ConsultaSerializers(data = request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'error': False,
                    'message': "Consulta Clinica Creada Con Exito",
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'error': True,
                    'message': "Invalid form",
                }, status=status.HTTP_400_BAD_REQUEST)

                   
    def put(self, request, pk):
        if request.method == 'PUT':
            save_consulta = get_object_or_404(Consulta.objects.all(), id=pk)
            serializer = ConsultaSerializers(instance=save_consulta, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({
                    'error': False,
                    'message': "Consulta liberada",
                    'product': serializer.data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'error': True,
                    'message': "Error Consulte al admin :v",
                }, status=status.HTTP_400_BAD_REQUEST)             


class EspecialistaView(APIView):
    def post (self,request):
        if request.method == 'POST':
            serializer = EspecialistaSerializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'error': False,
                    'message': "Especialista Clinico Creado Con Exito",
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'error': True,
                    'message': "Invalid form",
                }, status=status.HTTP_400_BAD_REQUEST)                

