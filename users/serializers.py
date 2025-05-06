from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    followees_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email',  'password', 'first_name', 'last_name','followees_count', 'subscription_type', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}
        extra_fields = ['followees_count']
        
    def get_followees_count(self, obj):
        return obj.following.count();    

    def create(self, validated_data):
        password = validated_data.pop('password')  # Remove password from validated_data
        user = User(**validated_data)  # Create user instance without saving
        user.set_password(password)  # Hash the password
        user.save()  # Save user to DB
        return user
    
    # def update(self, instance, validated_data):
    #     # Update user fields
    #     instance.email = validated_data.get('email', instance.email)

    #     # Update password if provided
    #     password = validated_data.get('password')
    #     if password:
    #         instance.set_password(password)

    #     instance.save()
    #     return instance
    
