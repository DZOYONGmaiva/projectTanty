from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from Evenement.models import Evenement
from Mediatheque.models import Photo, Video


def photo(request):
    evenements = Evenement.objects.all()
    photos = Photo.objects.all()
    l1 = []
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        eve = Evenement.objects.filter(nom__icontains=item_name)
        photos = Photo.objects.filter(Q(description__icontains=item_name) |
                                      Q(evenement__in=eve) |
                                      Q(date__icontains=item_name))
    for evenement in evenements:
        for photo in photos:
            if photo.evenement == evenement:
                if evenement in l1:
                    print(1)
                else:
                    l1.append(evenement)
    context = {"l1": l1, "photos": photos}
    return render(request, 'Médiathèque/photo.html', context)

def video(request):
    evenements = Evenement.objects.all()
    l2 = []
    videos = Video.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        eve = Evenement.objects.filter(nom__icontains=item_name)
        videos = Video.objects.filter(Q(description__icontains=item_name) |
                                      Q(evenement__in=eve) |
                                      Q(date__icontains=item_name))
    for evenement in evenements:
        for video in videos:
            if video.evenement == evenement:
                if evenement in l2:
                    print(1)
                else:
                    l2.append(evenement)
    context = {"l2": l2, "videos": videos}
    return render(request, 'Médiathèque/video.html', context)

def mediatheque(request):
    evenements = Evenement.objects.all()
    photos = Photo.objects.all()
    videos = Video.objects.all()

    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        eve = Evenement.objects.filter(nom__icontains=item_name)
        photos = Photo.objects.filter(Q(description__icontains=item_name) |
                                        Q(evenement__in=eve) |
                                      Q(date__icontains=item_name))
        videos = Video.objects.filter(Q(description__icontains=item_name) |
                                       Q(evenement__in=eve) |
                                      Q(date__icontains=item_name))
    l1 = []
    l2 = []
    v = 0
    for evenement in evenements:
        for photo in photos:
            if photo.evenement == evenement:
                if evenement in l1:
                    print(1)
                else:
                    l1.append(evenement)

    for evenement in evenements:
        for video in videos:
            if video.evenement == evenement:
                if evenement in l2:
                    print(1)
                else:
                    l2.append(evenement)

    context = {"l1":l1, "l2":l2, "photos":photos, "videos":videos}
    return render(request, 'Médiathèque/mediatheque.html', context)


def detailPhoto(request, myid):
    photo = get_object_or_404(Photo, id=myid)
    context = {"photo": photo}
    return render(request, 'Médiathèque/detailPhoto.html', context)

def detailVideo(request, myid):
    video = get_object_or_404(Video, id=myid)
    context = {"video": video}
    return render(request, 'Médiathèque/detailVideo.html', context)