from django.urls import path
from music.views import playlist_list,playlist_details,song_list,song_details

urlpatterns = [
    path('playlist',playlist_list),
    path('playlist/<int:pk>',playlist_details),
   path('songslist',song_list),
   path('songslist/<int:pk>',song_details)
]