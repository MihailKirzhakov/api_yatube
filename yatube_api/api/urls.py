from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from .views import GroupViewSet, PostViewSet, CommentViewSet


API_VERSION = 'v1'


router = routers.DefaultRouter()

router.register(
    f'{API_VERSION}/groups', GroupViewSet, basename='groups'
)
router.register(f'{API_VERSION}/posts', PostViewSet, basename='posts')
router.register(
    rf'{API_VERSION}/posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path(f'{API_VERSION}/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
