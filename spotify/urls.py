"""
URL configuration for spotify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.urls import user_urls, profile_urls
from artists.urls import artist_urls, follow_urls
from songs.urls import song_urls, interaction_urls, participant_urls
from albums.urls import album_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include(user_urls)),
    path('api/profiles/', include(profile_urls)),
    path('api/artists/', include(artist_urls)),
    path('api/follows/', include(follow_urls)),
    path('api/songs/', include(song_urls)),
    path('api/interactions/', include(interaction_urls)),
    path('api/participants/', include(participant_urls)),
    path('api/albums/', include(album_urls))
]
