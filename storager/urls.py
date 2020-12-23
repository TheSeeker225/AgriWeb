from django.urls import path

from . import views

urlpatterns = [
    path('login', views.connexion, name='connexion'),
    path('tableau-de-bord', views.index, name='dashboard'),
    path('liste-de-produits', views.catalogue, name='catalogue'),
    path('nouveau-produit', views.ajouterProduit, name='product-new'),

]