# tunr_app/serializers.py
from rest_framework import serializers

from .models import User, Resource


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'birthday')

class ResourceSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Artist
        fields = ('id', 'resource_name', 'resource_phone_number', 'resource_website', 'category', 'user')