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

    # def validate(self, data):
    #     request = self.context.get('request')
    #     if request and request.user and data.get('user') != request.user:
    #         raise serializers.ValidationError("You can only modify your own interactions.")
    #     return data

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

    participants = ParticipantSerializer(source='participant_set', many=True, read_only=True)
    interactions = InteractionSerializer(source='interaction_set', many=True, read_only=True)

    def create(self, validated_data):
        participants_data = validated_data.pop('participants', [])
        
        # Create Song object
        song = Song.objects.create(**validated_data)

        # Create Participants
        for participant_data in participants_data:
            artist = Artist.objects.get(id=participant_data['artist'])
            Participant.objects.create(song=song, artist=artist, role=participant_data['role'])

        return song

    def update(self, instance, validated_data):
        participants_data = validated_data.pop('participants', [])

        # Update Song fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update Participants (Clear and recreate)
        instance.participant_set.all().delete()
        for participant_data in participants_data:
            artist = Artist.objects.get(id=participant_data['artist'])
            Participant.objects.create(song=instance, artist=artist, role=participant_data['role'])

        return instance