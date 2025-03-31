from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer

# ✅ Create & List Users
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'first_name', 'last_name']

# ✅ Retrieve, Update & Delete User
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

User = get_user_model()
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)