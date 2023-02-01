
'''

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import SectorViewset, ManifestoeViewset,PollViewset, FGPollViewset, StatePollViewset

router = DefaultRouter()
router.register('admin/polls', PollViewset, basename='fgpolls')
router.register('admin/sectors', SectorViewset, basename='sector')
router.register('admin/manifestoe', ManifestoeViewset, basename='manifestoe')
router.register('fg', FGPollViewset, basename='fgpolls')

router.register('states', StatePollViewset, basename='statepoll')
#router.register('blogs', BlogAPI, basename='blogs')
'''
urlpatterns = [
    #path('blogs/', BlogAPI.as_view()),
]

#urlpatterns += router.urls
