from django.urls import path
from .views import PlaylistListCreate, PlaylistSongListCreate, PlayListDetail, PlaylistSongDetail

playlist_urls = [
    path("", PlaylistListCreate.as_view(), name="playlist-list-create"),
    path("<int:pk>/", PlayListDetail.as_view(), name="playlist-detail")
]

playlist_song_urls=[
    path("", PlaylistSongListCreate.as_view(), name="playlist-add-song"),
    path("<int:pk>/", PlaylistSongDetail.as_view(), name="playlist-song-detail")
]
