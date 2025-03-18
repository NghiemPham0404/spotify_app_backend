from django.urls import path,include

from .views import SongListCreate, SongDetailUpdateDelete, InteractionViewSet, ParticipantViewSet


song_urls =[
    path("", SongListCreate.as_view(), name = "song-list-create"),
    path("<int:pk>/", SongDetailUpdateDelete.as_view(), name = "song-detail")
]

interaction_urls = [
    path('', InteractionViewSet.as_view({'get': 'list', 'post': 'create'}), name='interaction-list'),
    path('<int:pk>/', InteractionViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='interaction-detail'),
]

participant_urls = [
    path("", ParticipantViewSet.as_view({'get':'list', 'post':'create'}), name='participant-list'),
    path('<int:pk>/', ParticipantViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='particitpant-detail')
]