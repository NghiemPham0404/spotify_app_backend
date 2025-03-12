from django.db import models
from songs.models import Song 
from artists.models import Artist
# Create your models here.
# Album
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True)
    publish_date = models.DateField(blank=True, null=True)

# Danh sách bài hát trong Album
class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    track_number = models.IntegerField()

    class Meta:
        unique_together = ('album', 'song')