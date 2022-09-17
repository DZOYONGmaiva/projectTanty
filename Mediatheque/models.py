from django.db import models

# Create your models here.
from Evenement.models import Evenement


class Photo(models.Model):
    photo = models.ImageField(upload_to="photos")
    description = models.TextField(blank=True)
    evenement = models.ForeignKey(Evenement, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']


class Video(models.Model):
    video = models.FileField(upload_to="videos")
    description = models.TextField(blank=True)
    evenement = models.ForeignKey(Evenement, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']