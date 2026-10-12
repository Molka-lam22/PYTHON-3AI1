from django.db import models
from EntrepriseApp.models import Entreprise
from django.core.exceptions import ValidationError
from django.utils import timezone


class Expedition(models.Model):
    reference = models.CharField(max_length=100, unique=True)
    ville_depart = models.CharField(max_length=100)
    ville_arrivee = models.CharField(max_length=100)
    poids_kg = models.DecimalField(max_digits=10, decimal_places=2)
    date_souhaitee = models.DateField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('terminee', 'Terminée'),
    ], default='en_attente')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relation avec le modèle Entreprise
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='expeditions')

    def clean(self):
        super().clean()
        if self.entreprise and self.entreprise.type_entreprise != 'chargeur':
            raise ValidationError({'entreprise': "Une expedition ne peut être que par une entreprise de type 'chargeur'"})
    @classmethod
    def _generate_reference(cls):
        annee = timezone.now().strftime('%Y')
        dernier =cls.objects.filter(reference__startswith=f"EXP_{annee}_").order_by('-reference').first()
        compteur = int(dernier.reference[-5:]) + 1 if dernier else 1
        if compteur > 99999:
            raise ValidationError("Limite exceeded")
        return f"EXP_{annee}_{compteur:05d}"

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = self._generate_reference()
        self.full_clean
        super().save(*args, **kwargs)