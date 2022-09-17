from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from Gamme.models import Gamme
from Mediatheque.models import Photo
from Produit.models import Produit
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    v = 0
    photos = Photo.objects.all()
    for photo in photos:
        if v == 0:
            actu = photo
            v = 1
    produits = Produit.objects.all()
    v = 0
    l = []
    for produit in produits:
        if v < 3:
            l.append(produit)
            v += 1
    context = {"actu": actu, 'l':l}
    return render(request, 'Produit/index.html', context)

def shop(request):
    produits = Produit.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        produits = Produit.objects.filter(Q(nom__icontains=item_name) |
                                          Q(prix__icontains=item_name) |
                                          Q(description__icontains=item_name) |
                                          Q(date__icontains=item_name))
    paginator = Paginator(produits, 3)
    page = request.GET.get('page')
    produits = paginator.get_page(page)
    gammes = Gamme.objects.all()
    context = {"produits": produits, "gammes":gammes}
    return render(request, 'Produit/shop.html', context)

def detail(request, myid):
    produit = get_object_or_404(Produit, id=myid)
    gammes = Gamme.objects.all()
    context = {"produit": produit, 'gammes':gammes}
    return render(request, 'Produit/detail.html', context)

def gamme(request, gam):
    gamme = get_object_or_404(Gamme, nom=gam)
    produits = Produit.objects.filter(gamme=gamme)
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        produits = Produit.objects.filter(Q(nom__icontains=item_name) |
                                          Q(prix__icontains=item_name) |
                                          Q(description__icontains=item_name) |
                                          Q(date__icontains=item_name))
    paginator = Paginator(produits, 3)
    page = request.GET.get('page')
    produits = paginator.get_page(page)
    gammes = Gamme.objects.all()
    context = {"produits": produits, "gammes": gammes}
    return render(request, 'Produit/gamme.html', context)

