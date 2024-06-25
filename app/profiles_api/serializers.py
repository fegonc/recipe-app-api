from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''Serializer for Hello API View'''
    name = serializers.CharField(max_length=10)