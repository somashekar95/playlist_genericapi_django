from django.shortcuts import render
from rest_framework import generics
from .serializer import songSerializer,playlistSerializer
from .models import playlist,song
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
class playList(generics.ListCreateAPIView):
    queryset=playlist.objects.all()
    serializer_class=playlistSerializer
    
class playlistList(generics.ListAPIView):
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

@csrf_exempt
def playlist_list(request):
    """
    Get all the playlist,or create playlist
    """
    if request.method == 'GET':
        play = playlist.objects.all()
        serializer=playlistSerializer(play , many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=playlistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def playlist_details(request,pk):
    """
    this is for GET,UPDATE and DELETE the playlist
    """
    try:
        play = playlist.objects.get(pk=pk)
    except playlist.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = playlistSerializer(play)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = playlistSerializer(play, data=data)
  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        play.delete()
        return HttpResponse(status=204)



@csrf_exempt
def song_list(request):
    """
    Get all the songslist,or create songslist
    """
    if request.method=='GET':
        songs=song.objects.all()
        serializer=songSerializer(songs,many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method=='POST':
        data = JSONParser().parse(request)
        serializer = songSerializer(dat=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def song_details(request,pk):
    """
    this is for GET,UPDATE and DELETE the songslist
    """
    try:
        songs=song.objects.get(pk=pk)
    except song.DoesNotExist:
        return HttpResponse(status=404)
    if request.method=='GET':
        serializer=songSerializer(songs)
        return JsonResponse(serializer.data,status=201)
    elif request.method=='POST':
        data = JSONParser.parse(request)
        serializer=songSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors,status=400)
    elif request.method=='DELETE':
        songs.delete()
        return HttpResponse(status=204)




