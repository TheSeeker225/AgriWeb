from django.contrib import admin

from .models import Categorie, Produit, Figurer, Commande

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Produit)
admin.site.register(Figurer)
admin.site.register(Commande)