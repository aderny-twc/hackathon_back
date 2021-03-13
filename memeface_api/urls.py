from django.urls import path, include
from rest_framework import routers
from .views import MemeViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register('memes', MemeViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]