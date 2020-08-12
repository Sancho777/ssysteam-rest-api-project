from rest_framework import serializers
from profiles_api import models
from rest_framework.response import Response


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ['id', 'email', 'name', 'department', 'password']
        field = ('id', 'email', 'name', 'department', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
                }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
        email = validated_data['email'],
        name = validated_data['name'],
        department = validated_data['department'],
        password = validated_data['password']
        )
        return user

    
    

    


        
