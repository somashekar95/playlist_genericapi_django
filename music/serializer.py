from rest_framework import serializers
from .models import playlist,song,list,user

class playlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = playlist
        fields ='__all__'

class songSerializer(serializers.ModelSerializer):
    class Meta:
        model = song
        fields ='__all__'

class listSerializer(serializers.ModelSerializer):
    class Meta:
        model = list
        fields ='__all__'

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields ='__all__'