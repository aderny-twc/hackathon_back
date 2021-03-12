from django.shortcuts import render
from rest_framework import viewsets

from .models import Meme, Rating
from .serializers import MemeSerializer, RatingSerializer


class MemeViewSet(viewsets.ModelViewSet):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer