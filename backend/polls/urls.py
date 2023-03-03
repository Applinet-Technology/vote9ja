


from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *
# PollViewset, FGPollViewset, StatePollViewset, StateCreateVote, Senatorial_districtPollViewset, Federal_ConstituentPollViewset, LGAPollViewset, State_ConstituentPollViewset, WardPollViewset,FGCreateVote, LGACreateVote,State_ConstituentCreateVote, State_ConstituentResultView, FGResultView, StateResultView, Senatorial_DistrictCreateVote, Senatorial_districtResultView, Federal_ConstituentCreateVote,Federal_ConstituentResultView,LGACreateVote, LGAResultView,WardCreateVote,WardResultView

router = DefaultRouter()
router.register('admin', PollViewset, basename='polls'),
router.register('fg', FGPollViewset, basename='fgpolls'),
router.register('state', StatePollViewset, basename='statepolls'),
router.register('senate', Senatorial_districtPollViewset, basename='senDicpolls'),
router.register('fed_con', Federal_ConstituentPollViewset, basename='fed_conpolls'),
router.register('lga', LGAPollViewset, basename='lgapolls'),
router.register('state_con', State_ConstituentPollViewset, basename='state_conpolls'),
router.register('ward', WardPollViewset, basename='wardpolls'),

urlpatterns = [
    path('vote/fg/<int:poll_pk>/<int:rating>', FGCreateVote.as_view(), name= 'federal_vote'),
    path('vote/state/<int:poll_pk>/<int:rating>', StateCreateVote.as_view(), name= 'state_vote'),
    path('result/fg', FGResultView.as_view()),
    path('result/state',StateResultView.as_view()),
    path('vote/sendis/<int:poll_pk>/<int:rating>', Senatorial_DistrictCreateVote.as_view()),
    path('result/sendis',Senatorial_districtResultView.as_view()),
    path('vote/fedcon/<int:poll_pk>/<int:rating>', Federal_ConstituentCreateVote.as_view()),
    path('result/fedcon', Federal_ConstituentResultView.as_view()),
    path('vote/lga/<int:poll_pk>/<int:rating>',LGACreateVote.as_view()),
    path('result/lga', LGAResultView.as_view()),
    path('vote/statecon/<int:poll_pk>/<int:rating>',State_ConstituentCreateVote.as_view()),
    path('result/statecon', State_ConstituentResultView.as_view()),
    path('vote/ward/<int:poll_pk>/<int:rating>',WardCreateVote.as_view()),
    path('result/ward',WardResultView.as_view()),

    
]

urlpatterns += router.urls
