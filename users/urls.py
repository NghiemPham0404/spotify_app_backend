from django.urls import path
from .views import UserListCreateView, UserDetailView, RegisterView

user_urls = [
    # User Endpoints
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]

register_urls = [
    path('', RegisterView.as_view(), name='register'),
]