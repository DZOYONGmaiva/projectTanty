from django.contrib import admin

# Register your models here.
from Produit.models import Produit

admin.site.site_header = "NTfoods-TANTY"
admin.site.site_title = "NTfoods"
admin.site.index_title = "Admin"

class AdminProduit(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'date', 'gamme')
    search_fields = ('nom',)
    list_editable = ('prix',)

admin.site.register(Produit, AdminProduit)
