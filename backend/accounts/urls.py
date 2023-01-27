
'''
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewset, BlogAPI

router = DefaultRouter()
router.register('users', UserViewset, basename='users')
#router.register('blogs', BlogAPI, basename='blogs')

urlpatterns = [
    path('blogs/', BlogAPI.as_view()),
]

urlpatterns += router.urls'''