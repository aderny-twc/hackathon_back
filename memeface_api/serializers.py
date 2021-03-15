from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Meme, Rating


class UserSerializer(serializers.ModelSerializer):
    """
    Provides an interface for creating a user.
    Prevents all users from being displayed.
    Generates a token for user access. 
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class MemeSerializer(serializers.ModelSerializer):
    """
    Content fields.
    Automatically records the current user when a new object is created.
    """
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Meme
        fields = '__all__'

    def create(self, validated_data):
        meme = Meme.objects.create(**validated_data)
        return meme


class RatingSerializer(serializers.ModelSerializer):
    """
    Rating fields.
    """
    class Meta:
        model = Rating
        fields = ('id', 'like', 'user', 'meme')


### USERS RATINGS SERIALIZATION
class RatingProfileSerializer(serializers.ModelSerializer):
    """
    Combines content and rating objects.
    """
    meme = serializers.ReadOnlyField(source='meme.id')

    class Meta:
        model = Rating
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Provides information about the user.
    """
    ratings = RatingProfileSerializer(source='rating_set',
                                        many=True,
                                        read_only=True)

    class Meta:
        model = User
        fields = ('ratings', 'id', 'username')


#TODO: Add automatic content and rating creation.
class MemeRatingSerializer(serializers.ModelSerializer):
    Ratings = serializers.StringRelatedField(many=True)

    class Meta:
        model = Rating
        fields = '__all__'
