from rest_framework import serializers

from .models import Meme, Rating


class MemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meme
        fields = ('id', 'title', 'image', 'description', 'user', 'like_rating', 'avg_rating')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'like', 'user', 'meme')
