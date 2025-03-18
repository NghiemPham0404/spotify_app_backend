from rest_framework import serializers

from artists.models import Artist
from users.models import User
from .models import Song, Participant, Interaction

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'
        
class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = '__all__'

    def validate(self, data):
        request = self.context.get('request')
        if request and request.user and data.get('user') != request.user:
            raise serializers.ValidationError("You can only modify your own interactions.")
        return data

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

    participants = ParticipantSerializer(source='participant_set', many=True, read_only=True)
    interactionSerializer = InteractionSerializer(source='Interaction', many=True, read_only=True)

    def create(self, validated_data):
        participants_data = validated_data.pop('participant_set', [])
        interactions_data = validated_data.pop('interaction_set', [])
        
        # Create Song object
        song = Song.objects.create(**validated_data)

        # Create Participants
        for participant_data in participants_data:
            artist = Artist.objects.get(id=participant_data['artist'])
            Participant.objects.create(song=song, artist=artist, role=participant_data['role'])

        # Create Interactions
        for interaction_data in interactions_data:
            user = User.objects.get(id=interaction_data['user'])
            Interaction.objects.create(song=song, user=user, interaction_type=interaction_data['interaction_type'])

        return song

    def update(self, instance, validated_data):
        participants_data = validated_data.pop('participant_set', [])
        interactions_data = validated_data.pop('interaction_set', [])

        # Update Song fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update Participants (Clear and recreate)
        instance.participant_set.all().delete()
        for participant_data in participants_data:
            artist = Artist.objects.get(id=participant_data['artist'])
            Participant.objects.create(song=instance, artist=artist, role=participant_data['role'])

        # Update Interactions (Clear and recreate)
        instance.interaction_set.all().delete()
        for interaction_data in interactions_data:
            user = User.objects.get(id=interaction_data['user'])
            Interaction.objects.create(song=instance, user=user, interaction_type=interaction_data['interaction_type'])

        return instance