from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from Partenaire.models import Partenaire


def affichePartenaire(request):
    partenaires = Partenaire.objects.all()

    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        partenaires = Partenaire.objects.filter(Q(nom__icontains=item_name) |
                                          Q(lien__icontains=item_name))
    context = {'partenaires':partenaires}
    return render(request, 'Partenaire/partenaire.html', context)