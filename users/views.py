from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer

# ✅ Create & List Users
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ✅ Retrieve, Update & Delete User
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ✅ Create & List Profiles
class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# ✅ Retrieve, Update & Delete Profile
class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
