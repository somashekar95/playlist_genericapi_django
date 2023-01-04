from django.db import models

# Create your models here.
class playlist(models.Model):
    playlist_id=models.AutoField(primary_key=True)
    playlist_name=models.CharField(max_length=10)

    def __str__(self):
        return self.playlist_name

class song(models.Model):
    song_id=models.AutoField(primary_key=True)
    song_name=models.CharField(max_length=100)
    url=models.URLField(max_length=200)

    def __str__(self):
        return self.song_name

class list(models.Model):
    list_id=models.AutoField(primary_key=True)
    playlist_id=models.ForeignKey(playlist,on_delete=models.CASCADE)
    song_id=models.ForeignKey(song,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.list_id)

class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    list_id=models.ForeignKey(list,on_delete=models.CASCADE)

    def __str__(self):
        return (self.user_id)

