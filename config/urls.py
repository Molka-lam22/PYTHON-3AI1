"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ExpeditionsApp import views 


urlpatterns = [
    #path('home/', home, name='home'),
    # Page principale du site : permet d'ouvrir la page d'acceuil home 127.0.0.1:8000/home 
    path('', views.home, name='home'),

    path('admin/', admin.site.urls),
    #path('expedition/', include('ExpeditionsApp.urls')),  #Include the URLs from the ExpeditionsApp
       
        # Page d'accueil
    path('expedition/', views.home, name='expedition_home'),

    # Afficher le nom
    path('expedition/afficher/<str:name>/', views.afficher, name='afficher'),

    # Liste des expéditions
    path('expedition/list/', views.listExpeditions, name='listExpeditions'),

    # Détail d'une expédition
    path('expedition/detail/<int:pk>/', views.detailExpedition, name='detailExpedition'),
]
