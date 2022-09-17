from django.db import models

# Create your models here.

class Gamme(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.nom