

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserListAPIView, UserViewsetAPIView, UserCreateAPIView

router = DefaultRouter()
router.register('users', UserViewsetAPIView, basename='users')


urlpatterns = [
    path('register/',UserCreateAPIView.as_view(), name='register'),
    path('users/', UserListAPIView.as_view(),name='users')
]

urlpatterns += router.urls