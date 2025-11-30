from django.db import models
from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE
# Create your models here.

class Concessionnaire(Model):
    nom = CharField(max_length=64)
    siret = CharField(max_length=14)



class Vehicule(Model):
    TYPE_CHOICES = [
        ('auto', 'Automobile'),
        ('moto', 'Moto'),
    ]
    type = CharField(max_length=4, choices=TYPE_CHOICES)
    marque = CharField(max_length=64)
    chevaux = models.IntegerField()
    prix_ht = models.FloatField()
    concessionnaire = ForeignKey(Concessionnaire, on_delete=CASCADE, related_name='vehicules')

