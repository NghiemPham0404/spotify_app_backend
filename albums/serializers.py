from rest_framework import serializers
from .models import Album
from songs.models import Song 
from songs.serializers import SongSerializer

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

    songs = SongSerializer(source = 'song_set', many = True)
