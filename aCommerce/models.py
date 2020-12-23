from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

class Produit(models.Model):
    categorie = models.ForeignKey(Categorie, models.SET_NULL, blank=True, null=True)
    nom = models.CharField(max_length=200)
    famille = models.CharField(max_length=21)
    couleur = models.CharField(max_length=7)
    prix = models.IntegerField(default=500)
    description = models.TextField()
    plus_info = models.TextField()
