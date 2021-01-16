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
    prix = models.FloatField()
    description = models.TextField()
    plus_info = models.TextField()

class Figurer(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Commande(models.Model):


    produits = models.ManyToManyField(Figurer)
    date_debut = models.DateTimeField(auto_now_add=True)
    jour_commande = models.DateTimeField()
