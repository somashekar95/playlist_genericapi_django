from rest_framework import serializers
from .models import playlist,song

class songSerializer(serializers.ModelSerializer):
    class Meta:
        model=song
        fields='__all__'


class playlistSerializer(serializers.ModelSerializer):
    # song=songSerializer(read_only=True,many=True)
    class Meta:
        model=playlist
        fields='__all__'