

'''
from django.shortcuts import render
from .serializers import *
#FGPollSerializer,PollSerializer, SectorSerializer, ManifestorSerializer
from rest_framework import viewsets
from .models import Sector, Manifestoe, Poll, FGPoll, StatePoll, Senatorial_districtPoll, Federal_ConstituentPoll, LGAPoll, State_ConstituentPoll, WardPoll



class SectorViewset(viewsets.ModelViewSet):
    queryset= Sector.objects.all()
    serializer_class=SectorSerializer
    
class ManifestoeViewset(viewsets.ModelViewSet):
    queryset= Manifestoe.objects.all()
    serializer_class=ManifestorSerializer



class PollViewset(viewsets.ModelViewSet):
    queryset= Poll.objects.all()
    serializer_class=PollSerializer


class FGPollViewset(viewsets.ModelViewSet):
    queryset= FGPoll.objects.all()
    serializer_class=FGPollSerializer
    

class StatePollViewset(viewsets.ModelViewSet):
    queryset= StatePoll.objects.all()
    serializer_class=StatePollSerializer



class Senatorial_districtPollViewset(viewsets.ModelViewSet):
    queryset= Senatorial_districtPoll.objects.all()
    serializer_class=Senatorial_districtPollSerializer


class Federal_ConstituentPollViewset(viewsets.ModelViewSet):
    queryset= Federal_ConstituentPoll.objects.all()
    serializer_class=Federal_ConstituentPollSerializer


class LGAPollViewset(viewsets.ModelViewSet):
    queryset= LGAPoll.objects.all()
    serializer_class=LGAPollSerializer


class State_ConstituentPollViewset(viewsets.ModelViewSet):
    queryset= State_ConstituentPoll.objects.all()
    serializer_class=State_ConstituentPollSerializer


class WardPollViewset(viewsets.ModelViewSet):
    queryset= WardPoll.objects.all()
    serializer_class=WardPollSerializer

'''
