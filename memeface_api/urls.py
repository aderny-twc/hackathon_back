from django.urls import path, include
from rest_framework import routers
from .views import MemeViewSet, RatingViewSet, UserViewSet
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('memes', MemeViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

