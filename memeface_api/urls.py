from django.urls import path, include
from rest_framework import routers
from .views import (MemeViewSet,
                    RatingViewSet,
                    UserViewSet,
                    UserProfileViewSet)


router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register('memes', MemeViewSet)
router.register('ratings', RatingViewSet)
router.register('user-profile', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
