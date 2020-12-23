from django.shortcuts import render

# Create your views here.
def connexion(request):
    return render(request, 'storager/index.html')
def index(request):
    return render(request, 'storager/dashboard.html')
def catalogue(request):
    return render(request, 'storager/produits/produits_list.html')
## Gestion de produits
def ajouterProduit(request):
    return render(request, 'storager/produits/produit-add.html')
def modifierProduit(request):
    return render(request, 'storager/produit-mod.html')
def supprimerProduit(request):
    return render(request, 'storager/produit-del.html')
## Gestion du personnel
def ajouterEmploye(request):
    return render(request, 'storager/employe-add.html')
def modifierEmploye(request):
    return render(request, 'storager/employe-mod.html')
def supprimerEmploye(request):
    return render(request, 'storager/employe-del.html')
## Gestion du materiel
def ajouterOutil(request):
    return render(request, 'storager/outil-add.html')
def modifierOutil(request):
    return render(request, 'storager/outil-mod.html')
def supprimerOutil(request):
    return render(request, 'storager/outil-del.html')
## Gestion des projets
def ajouterProjet(request):
    return render(request, 'storager/projet-add.html')
def modifierProjet(request):
    return render(request, 'storager/projet-mod.html')
def supprimerProjet(request):
    return render(request, 'storager/projet-del.html')
## Gestion des clients
def ajouterClient(request):
    return render(request, 'storager/client-add.html')
def modifierClient(request):
    return render(request, 'storager/client-mod.html')
def supprimerClient(request):
    return render(request, 'storager/client-del.html')
## Gestion des fournisseurs
def ajouterFournisseur(request):
    return render(request, 'storager/fournisseur-add.html')
def modifierFournisseur(request):
    return render(request, 'storager/fournisseur-mod.html')
def supprimerFournisseur(request):
    return render(request, 'storager/fournisseur-del.html')