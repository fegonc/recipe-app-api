from rest_framework import serializers

from core import models

class HelloSerializer(serializers.Serializer):
    '''Serializer for Hello API View'''
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    '''Serializer a user profile object'''

    class Meta:
        model = models.User
        fields = ['email', 'password', 'name', 'id']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type:': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)