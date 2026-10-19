from django.contrib import admin
from .models import Offre


@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = (
        "id", 
        "expedition", 
        "transporteur_nom", 
        "vehicule", 
        "prix",
        "delai_jours", 
        "status", 
        "created_at"
    )
    
    list_filter = ("status",)
    
    search_fields = (
        "expedition__reference", 
        "entreprise__raison_sociale", 
        "vehicule__immatriculation"
    )
    
    # 👈 Corrigé ici : 'entreprise' remplace 'transporteur'
    list_select_related = ("expedition", "entreprise", "vehicule")
    
    readonly_fields = ("created_at", "updated_at")
    
    fieldsets = (
        ("Offre", {
            "fields": ("expedition", "entreprise", "vehicule"),  
        }),
        ("Conditions", {
            "fields": ("prix", "delai_jours", "status"),
        }),
        ("Horodatage", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    @admin.display(description="Transporteur", ordering="entreprise__raison_sociale")
    def transporteur_nom(self, obj):
        return obj.entreprise.raison_sociale if obj.entreprise else "-" 