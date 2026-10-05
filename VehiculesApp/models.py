from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from EntrepriseApp.models import Entreprise


# Create your models here.
class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=10, unique=True)
    type_vehicule = models.CharField(max_length=50, choices=[('camion', 'Camion'), ('voiture', 'Voiture'), ('moto', 'Moto')])
    capacite_kg= models.PositiveIntegerField(validators=[MinValueValidator(1, "La capacité doit être supérieure à 0 kg")])
    disponible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    entreprise = models.ForeignKey('EntrepriseApp.Entreprise', on_delete=models.CASCADE, related_name='vehicules')
    offre = models.ForeignKey('OffreApp.Offre', on_delete=models.SET_NULL, null=True, blank=True, related_name='vehicules')