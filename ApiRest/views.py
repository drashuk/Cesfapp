from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from django.http import Http404, HttpResponse
# Create your views here.

# API ROOT ÚNICAMENTE PARA METODO GET 

class ApiRoot(generics.GenericAPIView):
    def get(self, request):
        return Response({
            'medicamentos': reverse('medicamentos', request=request),
            'fichas': reverse('ficha', request=request),
            'prescripcion': reverse('prescripcion', request=request),  
        })


# Excepcion del Token CSRF porque no hay login
@csrf_exempt
@api_view(['GET', 'POST'])

# Este metodo lista todos los medicamentos, o agrega un medicamento nuevo.
def medicamentos(request):
    if request.method == 'GET':
        medicamentos = Medicamento.objects.all()
        serializer = MedicamentoSerializer(medicamentos, many=True)
        if len(serializer.data) == 0:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND, content='No hay medicamentos para listar')
        else:
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MedicamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])

# Este metodo lista todas las fichas, o agrega una ficha nueva.
def ficha(request):
    if request.method == 'GET':
        fichas = Ficha.objects.all()
        serializer = FichaSerializer(fichas, many=True)
        if len(serializer.data) == 0:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND, content='No hay fichas para listar')
        else:
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FichaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])

# Este metodo lista todas las prescripciones, o agrega una prescripcion nueva.

def prescripcion(request):
    if request.method == 'GET':
        prescripciones = Prescripcion.objects.all()
        serializer = PrescripcionSerializer(prescripciones, many=True)
        if len(serializer.data) == 0:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND, content='No hay prescripciones para listar')
        else:
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PrescripcionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## GESTION DE LA API

@api_view(['PUT','DELETE','GET'])
# Este método gestiona un medicamento en especifico (debe introducir la ID), lo lista, lo actualiza o lo elimina.
def gestMed(request, id_medicamento):
    if request.method == 'GET':
        try:
            medicamento = Medicamento.objects.get(id_medicamento=id_medicamento)
            serializer = MedicamentoSerializer(medicamento)
            return Response(serializer.data)
        except Medicamento.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND, content="No existe el medicamento")
    try:
        medicamento = Medicamento.objects.get(id_medicamento=id_medicamento)
    except Medicamento.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, content="No existe el medicamento")

    if request.method == 'PUT':
        serializer = MedicamentoSerializer(medicamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            medicamento.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT','DELETE', 'GET'])
# Este método gestiona una ficha en especifico (debe introducir la ID), lo lista, lo actualiza o lo elimina.
def gestFicha(request, id_ficha):
    if request.method == 'GET':
        try:
            ficha = Ficha.objects.get(id_ficha=id_ficha)
            serializer = FichaSerializer(ficha)
            return Response(serializer.data)
        except Ficha.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND, content="No existe la ficha")
    try:
        ficha = Ficha.objects.get(id_ficha=id_ficha)
    except Ficha.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, content="No existe la ficha")

    if request.method == 'PUT':
        serializer = FichaSerializer(ficha, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            ficha.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT','DELETE', 'GET'])
# Este método gestiona una prescripcion en especifico (debe introducir la ID), lo lista, lo actualiza o lo elimina.
# OJO, al hacer PUT con ARC, Postman, SoapUI, debe saber el ID de la ficha que está asociada, y para actualizar el medicamento debe colocar el ID del medicamento.
def gestPrescripcion(request, id_prescripcion):
    if request.method == 'GET':
        try:
            prescripcion = Prescripcion.objects.get(id_prescripcion=id_prescripcion)
            serializer = PrescripcionSerializer(prescripcion)
            return Response(serializer.data)
        except Prescripcion.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND, content="No existe la prescripcion")
    try:
        prescripcion = Prescripcion.objects.get(id_prescripcion=id_prescripcion)
    except Prescripcion.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND, content="No existe la prescripcion")
    if request.method == 'PUT':
        serializer = PrescripcionSerializer(prescripcion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            prescripcion.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)