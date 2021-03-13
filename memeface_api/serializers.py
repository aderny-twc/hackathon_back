from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Meme, Rating


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class MemeSerializer(serializers.ModelSerializer):
    """Список всего контента."""
    class Meta:
        model = Meme
        fields = ('id', 'title', 'image', 'description', 'user', 'user_author', 'like_rating', 'avg_rating', 'created_at')

    def create(self, validated_data):
        meme = Meme.objects.create(**validated_data)
        return meme


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'like', 'user', 'meme')
