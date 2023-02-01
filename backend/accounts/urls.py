

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import user_list #BlogAPI

#router = DefaultRouter()
#router.register('users', UserViewset, basename='users')
#router.register('blogs', BlogAPI, basename='blogs')

urlpatterns = [
    path('users/', user_list,)
]

#urlpatterns += router.urls