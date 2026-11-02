from django.shortcuts import render

# Create your views here.
def home(request):
    return  HttpResponse("Bienvenue sur la page d'accueil de l'application des expéditions.")
