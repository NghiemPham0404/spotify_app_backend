from rest_framework import serializers
from .models import Album
from songs.models import Song 
from songs.serializers import SongSerializer

class AlbumSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()  # Include songs in Album response

    class Meta:
        model = Album
        fields = '__all__'

    def get_songs(self, obj):
        album_songs = Song.objects.filter(album=obj)
        return SongSerializer(album_songs, many=True).data
