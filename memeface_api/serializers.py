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
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    # print(user.pk_field)
    class Meta:
        model = Meme
        fields = (
        'id', 'title', 'image', 'description', 'user', 'user_author', 'like_rating', 'avg_rating', 'created_at')

    def create(self, validated_data):
        meme = Meme.objects.create(**validated_data)
        return meme


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'like', 'user', 'meme')


class RatingProfileSerializer(serializers.ModelSerializer):
    meme = serializers.ReadOnlyField(source='meme.id')

    class Meta:
        model = Rating
        fields = '__all__'


### USERS RATINGS SERIALIZATION
class UserProfileSerializer(serializers.ModelSerializer):
    ratings = RatingProfileSerializer(source='rating_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('ratings', 'id', 'username')


class MemeRatingSerializer(serializers.ModelSerializer):
    Ratings = serializers.StringRelatedField(many=True)

    class Meta:
        model = Rating
        fields = '__all__'

#
# ### MULTIPLE MODELS SERIALIZATION
# class MemeCreateSerializer(serializers.ModelSerializer):
#     """
#     Serializer to Add Meme model together with Rating model
#     """
#     user = serializers.PrimaryKeyRelatedField(
#         read_only=True,
#         default=serializers.CurrentUserDefault()
#     )
#
#     class RatingTempSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Rating
#             exclude = ['meme',]
#
#     rating = RatingTempSerializer()
#
#     class Meta:
#         model = Meme
#         fields = '__all__'
#
#     def create(self, validated_data, user=user):
#         rating_data = validated_data.pop('rating')
#         meme_obj = Meme.objects.create(**validated_data)
#         Rating.objects.create(meme=meme_obj.id, user=user.pk_field, **rating_data)
#         return meme_obj
#
#
# ## Writable nested serializers
#
# class MemeManySerializer(serializers.ModelSerializer):
#     meme = MemeSerializer()
#
#     class Meta:
#         model = Rating
#         fields = '__all__'
#
#     def create(self, validated_data):
#         memes_data = validated_data.pop('meme')
#         rating = Rating.objects.create(**validated_data)
#         # for meme_data in memes_data:
#         Meme.objects.create(**memes_data)
#         return rating