from django.contrib import admin
from .models import Artist, Follow
# Register your models here.
admin.site.register([Artist,Follow])