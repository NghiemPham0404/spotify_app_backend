from django.db import models
from albums.models import Album
from users.models import User
from artists.models import Artist

# Create your models here.
# Bài hát
class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=10, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    audio_file = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)

    album = models.ForeignKey(Album, on_delete=models.CASCADE,  null=True, blank=True)
    
    def __str__(self):
        return self.title
    

# Tham gia vào bài hát (ví dụ: ca sĩ hát chung, nhạc sĩ, producer)
class Participant(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)

    class Meta:
        unique_together = ('song', 'artist')

    def __str__(self):
        return self.song.__str__() + ", " + self.artist.__str__()

# Tương tác (Like, Share, Comment)
class Interaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)