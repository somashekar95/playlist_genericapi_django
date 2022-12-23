from django.db import models

# Create your models here.
class playlist(models.Model):
    playlist_id=models.CharField(max_length=200)
    playlist_name=models.CharField (max_length=50,unique=True)
    songs=models.CharField(max_length=100)
    user=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

def __str__(self):
    return self.playlist_name

class song(models.Model):
    song_id=models.CharField(max_length=10)
    playlist_name=models.ForeignKey(playlist,related_name='song',max_length=200,on_delete=models.CASCADE)
    song_name=models.CharField (max_length=50,unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
  
def __str__(self):
    return self.playlist_name