from django.urls import path,include

from .views import SongListCreate, SongDetailUpdateDelete
from .views import InteractionListCreate, InteractionDetail
from .views import ParticipantListCreate, ParticipantDetail


song_urls =[
    path("", SongListCreate.as_view(), name = "song-list-create"),
    path("<int:pk>/", SongDetailUpdateDelete.as_view(), name = "song-detail")
]

interaction_urls = [
    path('', InteractionListCreate.as_view(), name='interaction-list'),
    path('<int:pk>/', InteractionDetail.as_view() , name='interaction-detail'),
]

participant_urls = [
    path("", ParticipantListCreate.as_view(), name='participant-list'),
    path('<int:pk>/', ParticipantDetail.as_view(), name='particitpant-detail')
]