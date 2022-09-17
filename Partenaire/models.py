from django.db import models

# Create your models here.
class Partenaire(models.Model):
    nom = models.CharField(max_length=200)
    image = models.ImageField(upload_to="partenaires")
    lien = models.URLField(max_length=500)

    def __str__(self):
        return self.nom