from django.contrib import admin

# Register your models here.
from Mediatheque.models import Photo
from Mediatheque.models import Video

admin.site.register(Photo)
admin.site.register(Video)
