from django.urls import path
from .views import (
    ArtistListCreateView, ArtistDetailView,
    FollowArtistView, UnfollowArtistView,
    UserFollowedArtistsView, ArtistFollowersView
)

follow_urls = [
    # Follow & Unfollow
    path('<int:artist_id>/follow/', FollowArtistView.as_view(), name='follow-artist'),
    path('<int:artist_id>/unfollow/', UnfollowArtistView.as_view(), name='unfollow-artist'),
]

artist_urls = [
    # Artist Endpoints
    path('', ArtistListCreateView.as_view(), name='artist-list-create'),
    path('<int:pk>/', ArtistDetailView.as_view(), name='artist-detail'),
    path('<int:artist_id>/followers/', ArtistFollowersView.as_view(), name='artist-followers'),
]