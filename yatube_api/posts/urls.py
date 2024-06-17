# yatube_api/api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path(
        'api-token-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    path('', include(router.urls)),
]
