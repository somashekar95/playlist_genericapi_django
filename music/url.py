from django.contrib import admin
from django.urls import path
from .views import playlist_list,playlist_details,song_details,song_list,lists,list_details,user_details,user_list
from .views import playlists,playlistdetail,songslist,songsdetail,userlist,userdetail,listed,listdetail
urlpatterns = [
    path('playlist',playlist_list.as_view()),
    path('playlist/<int:pk>',playlist_details.as_view()),
    path('list',lists.as_view()),
    path('list/<int:pk>',list_details.as_view()),
    path('song',song_list.as_view()),
    path('song/<int:pk>',song_details.as_view()),
    path('user',user_list.as_view()),
    path('user/<int:pk>',user_details.as_view()),
    path('playlists',playlists),
    path('playlists/<int:pk>',playlistdetail),
    path('songs',songslist),
    path('songs/<int:pk>',songsdetail),
    path('users',userlist),
    path('users/<int:pk>',userdetail),
    path('lists',listed),
    path('lists/<int:pk>',listdetail),
    

]