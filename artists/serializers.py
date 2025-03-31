from rest_framework import serializers
from .models import Artist, Follow

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'  # Returns all fields

class ArtistSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = Artist
        fields = '__all__'
        extra_fields = ['followers_count']  # Ensure this is included if '__all__' is used

    def get_followers_count(self, obj):
        return obj.followers.count()  # Count number of followers for the artist