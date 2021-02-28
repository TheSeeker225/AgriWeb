from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('detail-du-parcours', views.parcours, name='detail-parcours'),
    path('nom-du-cours', views.course, name='detail-parcours'),

]