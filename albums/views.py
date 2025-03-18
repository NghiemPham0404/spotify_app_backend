from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Album
from .serializers import AlbumSerializer
from songs.models import Song

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

