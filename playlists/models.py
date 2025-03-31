from django.db import models
from songs.models import Song
from users.models import User
# Create your models here.
# Danh sách bài hát trong Playlist
# Playlist
class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    privacy_setting = models.CharField(max_length=50, blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.email + "-" + self.title

class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('playlist', 'song')