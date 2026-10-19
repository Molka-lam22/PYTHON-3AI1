from django.contrib import admin
from django.utils import timezone 
from .models import Expedition 

class EnRetardAdmin(admin.SimpleListFilter):
    title = 'en retard'
    parameter_name = 'en retard'

    def lookups(self, request, model_admin):
        return (
            ('en_attente', 'En attente'),
            ('en_cours', 'En cours'),
            ('terminee', 'Terminée'),
        )

    def queryset(self, request, queryset):
        aujourd_hui = timezone.now().date()
        if self.value() == 'en_attente':
            return queryset.filter(status='en_attente')
        elif self.value() == 'en_cours':
            return queryset.filter(status='en_cours')
        elif self.value() == 'terminee':
            return queryset.filter(status='terminee')


@admin.register(Expedition) 
class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('reference', 'ville_depart', 'ville_arrivee', 'poids_kg', 'date_souhaitee', 'status', 'entreprise', 'created_at', 'updated_at')
    list_filter = ('status', 'entreprise')
    search_fields = ('reference', 'ville_depart', 'ville_arrivee', 'entreprise__raison_sociale')
    list_select_related = ('entreprise',)
    list_editable = ('date_souhaitee',)
    ordering = ('date_souhaitee',)
    date_hierarchy = 'date_souhaitee'
    list_per_page = 25
    readonly_fields = ('reference', 'created_at', 'updated_at')
    
    fieldsets = (
        ("Éxpédition", {
            "fields": ('reference', 'entreprise', 'description')
        }),
        ("Itinéraire et poids", {
            "fields": ('ville_depart', 'ville_arrivee', 'poids_kg', 'date_souhaitee')
        }),
        ("Statut et horodatage", {
            "fields": ('status', 'created_at', 'updated_at')
        }),
    )