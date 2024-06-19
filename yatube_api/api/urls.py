from django.conf import settings
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from .views import GroupViewSet, PostViewSet, CommentViewSet


router = routers.DefaultRouter()

router.register(
    f'{settings.API_VERSION}/groups', GroupViewSet, basename='groups'
)
router.register(f'{settings.API_VERSION}/posts', PostViewSet, basename='posts')
router.register(
    rf'{settings.API_VERSION}/posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path(f'{settings.API_VERSION}/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
