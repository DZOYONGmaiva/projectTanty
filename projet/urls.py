from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from projet import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Produit.urls')),
    path('Commande', include('Commande.urls')),
    path('Utilisateur', include('Utilisateur.urls')),
    path('Partenaire', include('Partenaire.urls')),
    path('Mediatheque', include('Mediatheque.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
