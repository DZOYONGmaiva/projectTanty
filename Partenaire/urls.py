from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Partenaire import views
from projet import settings

urlpatterns = [
    path('affichePartenaire', views.affichePartenaire, name='affichePartenaire'),
]