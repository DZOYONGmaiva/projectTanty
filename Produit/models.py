from django.db import models

# Create your models here.
from django.urls import reverse
from Gamme.models import Gamme


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.FloatField(default=0.0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="produits")
    date = models.DateTimeField(auto_now_add=True)
    gamme = models.ForeignKey(Gamme, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.nom
