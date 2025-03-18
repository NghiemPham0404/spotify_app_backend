from django.db import models
from artists.models import Artist
# Create your models here.
# Album
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    creation_date = models.DateField(auto_now_add=True)
    publish_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title