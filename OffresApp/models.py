from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class Offre(models.Model):
    prix = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01, "Le prix doit être supérieur à 0")])
    delai_jours = models.IntegerField(validators=[MinValueValidator(1, "Le délai doit être d'au moins 1 jour")])
    status = models.CharField(max_length=20, choices=[
        ('proposee', 'Proposée'),
        ('en_attente', 'En attente'),
        ('acceptee', 'Acceptée'),
        ('refusee', 'Refusée'),
    ], default='proposee')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    # Relation avec le modèle Expedition
    expedition = models.ForeignKey('ExpeditionsApp.Expedition', on_delete=models.CASCADE, related_name='offres')
    # Relation avec le modèle Entreprise
    entreprise = models.ForeignKey('EntreprisesApp.Entreprise', on_delete=models.CASCADE, related_name='offres')
    # Relation avec le modèle Vehicule
    vehicule = models.ForeignKey('VehiculesApp.vehicule', on_delete=models.CASCADE, related_name='offres')

    def clean(self):
        super().clean()

        
        if self.entreprise and self.entreprise.type_entreprise != 'transporteur':
            raise ValidationError({'entreprise': "Une offre ne peut être créée que par une entreprise de type 'transporteur'"})

        if self.vehicule and self.entreprise and self.vehicule.entreprise != self.entreprise:
            raise ValidationError({'vehicule': "Le véhicule doit appartenir à la même entreprise que le transporteur"})
        if self.expedition and not self.expedition.peut_recevoir_offres():
            raise ValidationError({'expedition': "Une expédition ne peut recevoir de nouvelles offres que si son statut est 'publiee'"})

        # Règle 4: Une entreprise ne peut pas avoir deux offres au statut proposee actives sur la même expédition
        if self.entreprise and self.expedition and self.status == 'proposee':
            existing_offre = Offre.objects.filter(
                entreprise=self.entreprise,
                expedition=self.expedition,
                status='proposee'
            ).exclude(pk=self.pk).exists()
            if existing_offre:
                raise ValidationError({'expedition': "Cette entreprise a déjà une offre proposée sur cette expédition"})

        # Règle 6: Un véhicule dont disponible = False ne peut pas être proposé
        if self.vehicule and not self.vehicule.peut_etre_propose():
            raise ValidationError({'vehicule': "Ce véhicule n'est pas disponible"})

        # Règle 7: Vérification de la compatibilité du véhicule avec le poids de l'expédition
        if self.vehicule and self.expedition:
            poids_expedition = float(self.expedition.poids_kg)
            type_vehicule = self.vehicule.type_vehicule

            capacites_min = {
                'camionnette': 0,
                'camion_porte': 3500,
                'semi_remorque': 19000,
                'fourgon': 3500,
            }

            capacites_max = {
                'camionnette': 1500,
                'camion_porte': 19000,
                'semi_remorque': 26000,
                'fourgon': 3500,
            }

            if capacites_min[type_vehicule] and poids_expedition < capacites_min[type_vehicule]:
                raise ValidationError({'vehicule': f"Le véhicule de type '{type_vehicule}' n'est pas adapté pour ce poids (minimum: {capacites_min[type_vehicule]} kg)"})

            if poids_expedition > capacites_max[type_vehicule]:
                raise ValidationError({'vehicule': f"Le véhicule de type '{type_vehicule}' ne peut pas transporter ce poids (maximum: {capacites_max[type_vehicule]} kg)"})

    def save(self, *args, **kwargs):
        # Règle 5: Cascade à l'acceptation
        if self.status == 'acceptee':
            # Mettre l'expédition à 'attribuée'
            self.expedition.status = 'attribuée'
            self.expedition.save()

            # Refuser toutes les autres offres 'proposee' sur cette expédition
            Offre.objects.filter(
                expedition=self.expedition,
                status='proposee'
            ).exclude(pk=self.pk).update(status='refusee')

        self.full_clean()
        super().save(*args, **kwargs)
