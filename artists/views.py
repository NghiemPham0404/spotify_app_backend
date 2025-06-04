from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Artist, Follow
from .serializers import ArtistSerializer, FollowSerializer

# Artist List & Create
class ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']  # Assuming 'name' is a field in the Artist model

# Artist Detail (Retrieve, Update, Delete)
class ArtistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# Follow an Artist
class FollowArtistView(generics.CreateAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]  # User must be logged in

    def create(self, request, *args, **kwargs):
        follower = request.user  # Authenticated user
        followee_id = self.kwargs.get("artist_id")
        
        try:
            followee = Artist.objects.get(id=followee_id)
            follow, created = Follow.objects.get_or_create(follower=follower, followee=followee)
            if created:
                return Response({"message": "Followed successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "Already following"}, status=status.HTTP_200_OK)
        except Artist.DoesNotExist:
            return Response({"error": "Artist not found"}, status=status.HTTP_404_NOT_FOUND)

# Unfollow an Artist
class UnfollowArtistView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        follower = request.user
        followee_id = self.kwargs.get("artist_id")

        try:
            follow = Follow.objects.get(follower=follower, followee_id=followee_id)
            follow.delete()
            return Response({"message": "Unfollowed successfully"}, status=status.HTTP_200_OK)
        except Follow.DoesNotExist:
            return Response({"error": "Not following this artist"}, status=status.HTTP_400_BAD_REQUEST)
