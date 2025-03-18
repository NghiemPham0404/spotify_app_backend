from django.shortcuts import render

from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from .models import Song, Participant, Interaction
from .serializers import SongSerializer, ParticipantSerializer, InteractionSerializer

class SongListCreate(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer

    def get_queryset(self):
        """Filter interactions so users can only see their own."""
        return Interaction.objects.filter(user=self.request.user)

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


