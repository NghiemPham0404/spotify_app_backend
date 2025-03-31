from django.urls import path
from .views import UserListCreateView, UserDetailView, RegisterView
from artists.views import UserFollowedArtistsView

user_urls = [
    # User Endpoints
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Get Follow Data
    path('user/followed-artists/', UserFollowedArtistsView.as_view(), name='user-followed-artists'),
]

register_urls = [
    path('', RegisterView.as_view(), name='register'),
]