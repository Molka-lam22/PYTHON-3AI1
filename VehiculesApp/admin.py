from django.contrib import admin
from .models import Vehicule


# Register your models here.
@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('immatriculation', 'type_vehicule', 'capacite_kg', 'disponible', 'entreprise')
    list_filter = ('type_vehicule', 'disponible', 'entreprise')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ("Informations du véhicule", {"fields": ('immatriculation', 'type_vehicule', 'capacite_kg', 'disponible') }),
        ("Entreprise", {"fields": ('entreprise',)}),
        ("Horodatage", {"fields": ('created_at', 'updated_at')}),
    )