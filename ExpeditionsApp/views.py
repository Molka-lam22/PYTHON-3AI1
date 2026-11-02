from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from ExpeditionsApp.models import Expedition


def home(request):
    return HttpResponse("Welcome to the Expedition App!")


def afficher(request, name):
    return render(request, 'expedition/afficher.html', {'name': name})

def listExpeditions(request):
    # Logic to retrieve and display a list of expeditions
    expeditions = Expedition.objects.all()  # Assuming you have an Expedition model
    return render(request, 'expedition/list.html', {'expeditions': expeditions})


def detailExpedition(request, pk):
    #expedition = Expedition.objects.get(pk=pk)
    expedition = get_object_or_404(Expedition, pk=pk)
    return render(request, 'expedition/detail.html', {'expedition': expedition}) 
# Create your views here.
