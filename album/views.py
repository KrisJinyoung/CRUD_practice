from django.shortcuts import render
from .models import Album

# Create your views here.

def album(request):
    albums = Album.objects
    return render(request, 'album.html',{'albums':albums})