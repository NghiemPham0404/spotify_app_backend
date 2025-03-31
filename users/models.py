from django.db import models
from django.contrib.auth.models import AbstractUser

# Người dùng (Kế thừa từ AbstractUser để hỗ trợ login)
class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    subscription_type = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.CharField(max_length=255, blank=True, null=True)

    username = None  # Xóa username
    def __str__(self):
        return self.email
