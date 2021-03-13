from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Meme, Rating
from .serializers import MemeSerializer, RatingSerializer


class MemeViewSet(viewsets.ModelViewSet):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer

    @action(detail=True, methods=['POST'])
    def rate_meme(self, request, pk=None):
        if 'likes' in request.data:
            meme = Meme.objects.get(id=pk)
            likes = request.data['likes']
            # user = request.user
            user = User.objects.get(id=1)

            try:
                rating = Rating.objects.get(user=user, meme=meme, )
                rating.like = likes
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(user=user, meme=meme, like=likes)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)


        else:
            respone = {'message': 'You need to provide likes'}
            return Response(respone, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
