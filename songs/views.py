from django.shortcuts import render

from rest_framework import viewsets, generics, filters
from rest_framework.response import Response
from rest_framework import status
from .models import Song, Participant, Interaction
from .serializers import SongSerializer, ParticipantSerializer, InteractionSerializer

class SongListCreate(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class SongDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    filter_backends = [filters.SearchFilter]
    filters_fields = ['song__title', 'user__username', 'interaction_type']

    def update(self, request, *args, **kwargs):
        """Ensure only the interaction owner can update."""
        instance = self.get_object()
        if instance.user != request.user:
            return Response({"error": "You can only update your own interactions."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Ensure only the interaction owner can delete."""
        instance = self.get_object()
        if instance.user != request.user:
            return Response({"error": "You can only delete your own interactions."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


