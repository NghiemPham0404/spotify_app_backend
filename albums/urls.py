from django.urls import path, include
from .views import AlbumViewSet

album_urls=[
    path('', AlbumViewSet.as_view({'get': 'list', 'post': 'create'}), name = 'album-list'),
    path('<int:pk>/', AlbumViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='album-detail')
]
