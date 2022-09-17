from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Produit import views
from projet import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('detail/<int:myid>/', views.detail, name='detail'),
    path('gamme/<str:gam>/', views.gamme, name='gamme'),
]