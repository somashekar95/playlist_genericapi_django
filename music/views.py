from rest_framework import serializers
from .models import playlist,song,list,user
from .serializer import playlistSerializer,songSerializer,listSerializer,userSerializer
from rest_framework import generics
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
  
# Create your views here.

class playlist_list(generics.ListCreateAPIView):
    queryset=playlist.objects.all()
    serializer_class=playlistSerializer

class playlist_details(generics.RetrieveUpdateDestroyAPIView):
    queryset=playlist
    serializer_class=playlistSerializer

class song_list(generics.ListCreateAPIView):
    queryset=song.objects.all()
    serializer_class=songSerializer

class song_details(generics.RetrieveUpdateDestroyAPIView):
    queryset=song
    serializer_class=songSerializer

class lists(generics.ListCreateAPIView):
    queryset=list.objects.all()
    serializer_class=listSerializer

class list_details(generics.RetrieveUpdateDestroyAPIView):
    queryset=list
    serializer_class=listSerializer

class user_list(generics.ListCreateAPIView):
    queryset=user.objects.all()
    serializer_class=userSerializer

class user_details(generics.RetrieveUpdateDestroyAPIView):
    queryset=user
    serializer_class=userSerializer


# Function Based Api
@csrf_exempt
def playlists(request):
    """
    List all playlists, or create a new playlist
    """
    if request.method == 'GET':
        playlists = playlist.objects.all()
        serializer = playlistSerializer(playlists, many=True)
        return JsonResponse(serializer.data, safe=False)
  
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = playlistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
  
@csrf_exempt
def playlistdetail(request, pk):
    try:
        playlists = playlist.objects.get(pk=pk)
    except playlist.DoesNotExist:
        return HttpResponse(status=404)
  
    if request.method == 'GET':
        serializer = playlistSerializer(playlists)
        return JsonResponse(serializer.data)
  
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = playlistSerializer(playlist, data=data)
  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        playlist.delete()
        return HttpResponse(status=204)

@csrf_exempt
def songslist(request):
    """
    List all songss, or create a new songs
    """
    if request.method == 'GET':
        songs = song.objects.all()
        serializer = songSerializer(songs, many=True)
        return JsonResponse(serializer.data, safe=False)
  
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = songSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
  
@csrf_exempt
def songsdetail(request, pk):
    try:
        songs = song.objects.get(pk=pk)
    except song.DoesNotExist:
        return HttpResponse(status=404)
  
    if request.method == 'GET':
        serializer = songSerializer(songs)
        return JsonResponse(serializer.data)
  
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = songSerializer(songs, data=data)
  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        songs.delete()
        return HttpResponse(status=204)

@csrf_exempt
def listed(request):
    """
    List all lists, or create a new list
    """
    if request.method == 'GET':
        lists = list.objects.all()
        serializer = listSerializer(lists, many=True)
        return JsonResponse(serializer.data, safe=False)
  
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = listSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
  
@csrf_exempt
def listdetail(request, pk):
    try:
        lists = list.objects.get(pk=pk)
    except list.DoesNotExist:
        return HttpResponse(status=404)
  
    if request.method == 'GET':
        serializer = listSerializer(lists)
        return JsonResponse(serializer.data)
  
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = listSerializer(list, data=data)
  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        lists.delete()
        return HttpResponse(status=204)

@csrf_exempt
def userlist(request):
    """
    List all users, or create a new user
    """
    if request.method == 'GET':
        users = user.objects.all()
        serializer = userSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
  
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = userSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
  
@csrf_exempt
def userdetail(request, pk):
    try:
        users = user.objects.get(pk=pk)
    except user.DoesNotExist:
        return HttpResponse(status=404)
  
    if request.method == 'GET':
        serializer = userSerializer(users)
        return JsonResponse(serializer.data)
  
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = userSerializer(user, data=data)
  
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
  
    elif request.method == 'DELETE':
        users.delete()
        return HttpResponse(status=204)

    