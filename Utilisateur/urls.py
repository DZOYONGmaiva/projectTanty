from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Utilisateur import views
from projet import settings

urlpatterns = [
    path('', views.compte, name='compte'),
    path('contact', views.Contacter, name='contact'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('aPropos', views.aPropos, name='aPropos'),
    path('carriere', views.carriere, name='carriere'),
    path('Contacter', views.contact, name='Contacter'),
    path('modifCompte', views.modifCompte, name='modifCompte'),
]