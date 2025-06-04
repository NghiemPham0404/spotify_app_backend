from django.urls import path
from .views import deepseek_view

chatbot_url = [
    path("", deepseek_view),
]
