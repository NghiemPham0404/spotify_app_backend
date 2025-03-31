from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Playlist, PlaylistSong
from .serializers import PlaylistSerializer, PlaylistSongSerializer

# API to create and list playlists
class PlaylistListCreate(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlayListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

# API to add songs to a playlist
class PlaylistSongListCreate(generics.ListCreateAPIView):
    queryset = PlaylistSong.objects.all()
    serializer_class = PlaylistSongSerializer

class PlaylistSongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlaylistSong.objects.all()
    serializer_class = PlaylistSongSerializer  
