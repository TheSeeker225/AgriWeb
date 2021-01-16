from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('produits', views.produits, name='catalogue'),
    path('produits/<categorie_nom>', views.categorie, name='categorie'),
    path('produits/<categorie_nom>/<produit_nom>', views.produit, name='produit'),
    path('panier/consulter', views.panier, name='voir-panier'),
    path('panier/valider', views.checkout, name='checkout'),
    path('panier/confirmation', views.confirmation, name='confirmation'),
    path('articles/', views.blog, name='blog'),
    path('articles/<slug>', views.article, name='article'),
    path('a-propos', views.about, name='contact-us'),
    path('contact', views.contact, name='contact-us'),

]