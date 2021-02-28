from django.http import HttpResponse
from django.shortcuts import render
from .models import Categorie, Produit, Figurer, Commande



# Create your views here.
def homepage(request):
    return render(request, 'aCommerce/index.html')
def produits(request):
    context = {
        'categorie_list': Categorie.objects.all(),
        'produit_list': Produit.objects.all(),
    }
    return render(request, 'aCommerce/catalogue.html', context)

def categorie(request, categorie_nom):
    return HttpResponse("Hello, world ! It is there I show the description of a product")
def produit(request, categorie_nom = "Legumes", produit_nom = "Aubergine"):
    return render(request, 'aCommerce/product-detail.html')
def panier(request):
    return render(request, 'aCommerce/cart.html')
def checkout(request):
    return HttpResponse("Hello, world ! It is there I show cart content.")
def confirmation(request):
    return HttpResponse("Hello, world ! It is there I show cart content.")
def blog(request):
    return render(request, 'aCommerce/blog.html')
def article(request, slug = "Hello world"):
    return render(request, 'aCommerce/blog-detail.html')
def about(request):
    return render(request, 'aCommerce/about.html')
def contact(request):
    return render(request, 'aCommerce/contact.html')