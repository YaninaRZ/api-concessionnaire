from rest_framework.serializers import ModelSerializer
from .models import Concessionnaire, Vehicule

class ConcessionnaireSerializer(ModelSerializer):
    class Meta:
        model = Concessionnaire
        fields = ['nom']

class VehiculeSerializer(ModelSerializer):
    class Meta:
        model = Vehicule
        fields = '__all__'