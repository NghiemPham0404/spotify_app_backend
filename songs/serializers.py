from rest_framework import serializers

from artists.models import Artist
from users.models import User
from .models import Song, Participant, Interaction

class ParticipantSerializer(serializers.ModelSerializer):
    artist_name = serializers.SerializerMethodField()
    class Meta:
        model = Participant
        fields = '__all__'

    def get_artist_name(self, obj):
        return obj.artist.name if obj.artist else None

        
class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

    participants = ParticipantSerializer(source='participant_set', many=True, read_only=True)