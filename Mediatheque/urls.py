from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Mediatheque import views
from projet import settings

urlpatterns = [
    path('photo', views.photo, name='photo'),
    path('video', views.video, name='video'),
    path('mediatheque', views.mediatheque, name='mediatheque'),
    path('detailPhoto/<int:myid>/', views.detailPhoto, name='detailPhoto'),
    path('detailVideo/<int:myid>/', views.detailVideo, name='detailVideo'),
]