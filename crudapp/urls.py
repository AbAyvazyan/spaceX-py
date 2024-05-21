from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostCRUDViewSet

router = DefaultRouter()
router.register('posts', PostCRUDViewSet, basename='post')

urlpatterns = router.urls
