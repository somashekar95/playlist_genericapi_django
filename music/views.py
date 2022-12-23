from django.shortcuts import render
from rest_framework import generics
from .serializer import songSerializer,playlistSerializer
from .models import playlist,song

# Create your views here.
class playList(generics.ListCreateAPIView):
    queryset=playlist.objects.all()
    serializer_class=playlistSerializer

class playlistDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=playlist
    serializer_class=playlistSerializer

class songlist(generics.ListCreateAPIView):
    queryset=song.objects.all()
    serializer_class=songSerializer

class songDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=song
    serializer_class=songSerializer
