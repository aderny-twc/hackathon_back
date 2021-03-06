from django.contrib.auth.models import User
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from .models import Meme, Rating
from .serializers import (MemeSerializer,
                            RatingSerializer,
                            UserSerializer,
                            UserProfileSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """
    Interfaces for working with user objects.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MemeViewSet(viewsets.ModelViewSet):
    """
    Provides work with content.
    Checks the content of the user's response. 
    Available to authorized users only.
    """
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @action(detail=True, methods=['POST'])
    def rate_meme(self, request, pk=None):
        if 'likes' in request.data:
            meme = Meme.objects.get(id=pk)
            likes = request.data['likes']
            user = request.user

            try:
                rating = Rating.objects.get(user=user, meme=meme, )
                rating.like = likes
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating updated',
                            'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, meme=meme, like=likes)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating created',
                            'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)


        else:
            respone = {'message': 'You need to provide likes'}
            return Response(respone, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    """
    Information about user ratings.
    Available to authorized users only.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response = {'message': 'You can\'t update rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You can\'t create rating like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    User information.
    Available to authorized users only. 
    """
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

