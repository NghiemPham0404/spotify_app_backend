from django.urls import path
from .views import UserListCreateView, UserDetailView, ProfileListCreateView, ProfileDetailView
from artists.views import UserFollowedArtistsView

user_urls = [
    # User Endpoints
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Get Follow Data
    path('user/followed-artists/', UserFollowedArtistsView.as_view(), name='user-followed-artists'),
]

profile_urls = [
    # Profile Endpoints
    path('', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
]