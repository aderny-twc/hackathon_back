from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Meme, Rating


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = ('id', 'title', 'image', 'description', 'user', 'like_rating', 'avg_rating')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'like', 'user', 'meme')
