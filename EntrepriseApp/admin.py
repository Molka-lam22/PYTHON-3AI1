from django.contrib import admin
from .models import Entreprise 
from .models import Utilisateur


# Register your models here.

@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ('raison_sociale', 'matricule_fiscale', 'type_entreprise', 'gerant', 'created_at', 'updated_at')
    list_filter = ('type_entreprise', 'created_at')
    search_fields = ('raison_sociale', 'matricule_fiscale', 'gerant__username', "gerant_email")
    list_select_related = ('gerant',)
    list_editable = ('type_entreprise',)
    date_hierarchy = 'created_at'
    list_per_page = 25
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'role', 'telephone', 'is_active', 'created_at', 'updated_at')
    list_filter = ('role', 'is_active', 'is_superuser')
    search_fields = ('user_id', 'username', 'email')
    readonly_fields = ('user_id', 'date_joined', 'last_login', 'created_at', 'updated_at')
    fieldsets = (
        ("Informations personnelles", {"fields": ('username', 'email', 'first_name', 'last_name', 'telephone')}),
        ("Permissions", {"fields": ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ("Horodatage", {"fields": ('date_joined', 'last_login', 'created_at', 'updated_at')}),

    )