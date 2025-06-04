from django.db import models
from users.models import User

# Create your models here.
# Nghệ sĩ
class Artist(models.Model):
    name = models.CharField(max_length=255)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name        
    

# Quan hệ Follow giữa User và Artist
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    followee = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="followers")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'followee')