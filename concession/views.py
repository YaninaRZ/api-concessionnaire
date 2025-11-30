from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from concession.models import Vehicule, Concessionnaire
from concession.serializers import VehiculeSerializer, ConcessionnaireSerializer
# Create your views here.

class ConcessionnaireListView(APIView):
    def get(self, request):
        concessionnaires = Concessionnaire.objects.all()
        serializer = ConcessionnaireSerializer(concessionnaires, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ConcessionnaireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class ConcessionnaireDetailView(APIView):
    def get(self, request, pk):
        concessionnaire = get_object_or_404(Concessionnaire, pk=pk)
        serializer = ConcessionnaireSerializer(concessionnaire)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        concessionnaire = get_object_or_404(Concessionnaire, pk=pk)
        concessionnaire.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    
class VehiculeListView(APIView):
    def get(self, request, concessionnaire_id):
        vehicules = Vehicule.objects.filter(concessionnaire_id=concessionnaire_id)
        serializer = VehiculeSerializer(vehicules, many=True)
        return Response(serializer.data)
    
    def post(self, request, concessionnaire_id):
        concessionnaire = get_object_or_404(Concessionnaire, pk=concessionnaire_id)
        serializer = VehiculeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(concessionnaire=concessionnaire)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class VehiculeDetailView(APIView):
    def get(self, request, concessionnaire_id, vehicule_id):
        vehicule = get_object_or_404(Vehicule, pk=vehicule_id, concessionnaire_id=concessionnaire_id)
        serializer = VehiculeSerializer(vehicule)
        return Response(serializer.data)