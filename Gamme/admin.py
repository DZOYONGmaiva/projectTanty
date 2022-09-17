from django.contrib import admin

# Register your models here.
from Gamme.models import Gamme

class AdminGamme(admin.ModelAdmin):
    list_display = ('nom', 'date' )

admin.site.register(Gamme, AdminGamme)
