
from django.http.response import JsonResponse
import datetime
from django.shortcuts import render
from .serializers import *
FGPollSerializer,PollSerializer,FGPollSerializer, StatePollSerializer, Senatorial_districtPollSerializer, Federal_ConstituentPollSerializer, LGAPollSerializer, State_ConstituentPollSerializer, WardPollSerializer, FGVoteSerializer, StateVoteSerializer, Senatorial_districtVoteSerializer, Federal_ConstituentVoteSerializer, LGAVoteSerializer, State_ConstituentVoteSerializer, WardVoteSerializer, ResultSerializer

from rest_framework import status, viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from .models import Poll, FGPoll, StatePoll, Senatorial_districtPoll, Federal_ConstituentPoll, LGAPoll, State_ConstituentPoll, WardPoll, FGVote, StateVote, Senatorial_districtVote, Federal_ConstituentVote, LGAVote, State_ConstituentVote, WardVote, Result

from politicians.models import Presidency,PresidencyCandidateManifestoeDetail, PresidencyParty, PoliticalParty, Presidential,Guber,GuberParty, Senate, SenateParty, Fed_Rep, Fed_RepParty,Chairmanship, ChairmanshipParty, State_Rep, State_RepParty, Councilorship, CouncilorshipParty
from accounts.models import Senatorial_district
from political_parties.parties.inec_parties import REGISTERED_PARTIES
from .models.polls import CHOICE
from accounts.models import User



class PollViewset(viewsets.ModelViewSet):
    permission_classes=(IsAdminUser,)
    queryset= Poll.objects.all()
    serializer_class=PollSerializer


class FGPollViewset(viewsets.ModelViewSet):
    permission_classes =(IsAdminUser,)
    queryset= FGPoll.objects.all()
    serializer_class=FGPollSerializer

# class FGVoteViewset(viewsets.ModelViewSet):
#     queryset= FGVote.objects.all()
#     serializer_class=FGVoteSerializer
    
class FGCreateVote(APIView):
    permission_classes= (IsAdminUser, IsAuthenticated,)
    serializer_class = FGVoteSerializer
    def post(self, request, poll_pk, rating):
        # presidency=Presidential.objects.get(pk=1)
        # print(presidency.party)
        poll = FGPoll.objects.get(pk=poll_pk)
        print(poll.manifestoe)
        print(int(poll.party.party.name))
        voter= request.user
        user = User.objects.get(username=voter)
        party = int(poll.party.party.name)
        
        data = {'voter': user.id, 'poll': poll_pk,'rating': rating}
        print(data)
        serializer = FGVoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FGResultView(APIView):
    def get(self, request):
        voter= request.user
        #print(voter)
        user = User.objects.get(username=voter)
        poll = FGPoll.objects.get(pk=1)
        presidency=poll.presidency
        votes=FGVote.objects.all()
        count_all = votes.count()
        count_0 = FGVote.objects.filter(rating=CHOICE[0][0]).count()
        count_1 = FGVote.objects.filter(rating=CHOICE[1][0]).count()
        count_2 = FGVote.objects.filter(rating=CHOICE[2][0]).count()
        count_3 = FGVote.objects.filter(rating=CHOICE[3][0]).count()
        count_4 = FGVote.objects.filter(rating=CHOICE[4][0]).count()
        count_5 = FGVote.objects.filter(rating=CHOICE[5][0]).count()
        
        vote_0 = int(count_0) * 0
        vote_1 = int(count_1) * 1
        vote_2 = int(count_2) * 2
        vote_3 = int(count_3) * 3
        vote_4 = int(count_4) * 4
        vote_5 = int(count_5) * 5
        
        vote_all= int(count_all) * 5
        
        
        if count_all ==0:
            return f'No user has voted yet!!!'
        vote_total = vote_0 + vote_1 + vote_2 + vote_3 + vote_4  + vote_5
        #poll = FGPoll.objects.get(presidency=1)
        #party =int(poll.party.party.name)
        party =PresidencyParty.objects.get(presidency=1).party.get_party_name
        print(party)
        result= int((vote_total/vote_all)*100)
        data = {'presidency':{'president':presidency.president.presidency, 'vice_president':presidency.vice_president.presidency,'party':party},'result':f'{result}%','checker':user.get_full_name, 'date':datetime.datetime.now()
        }
        print(data)
        #print(result)
        return Response(data)
        
        



class StatePollViewset(viewsets.ModelViewSet):
    permission_classes=(IsAdminUser, IsAuthenticated,)
    queryset= StatePoll.objects.all()
    serializer_class=StatePollSerializer


# class StateVoteViewset(viewsets.ModelViewSet):
#     queryset= StateVote.objects.all()
#     serializer_class=StateVoteSerializer

class StateCreateVote(APIView):
    permission_classes=(IsAdminUser, IsAuthenticated,)
    serializer_class = StateVoteSerializer
    def post(self, request, poll_pk, rating):
        voter= request.user
        user = User.objects.get(username=voter)
        print(user.state.name)
        state=int(user.state.name)
        guber = Guber.objects.get(state=state)
        #print(guber)
        poll = StatePoll.objects.get(pk=poll_pk)
        print(poll.manifestoe)
        print(poll.party.party.party.name)
        
        
        party = int(poll.party.party.party.name)
        data = {'state':state,'party':party,'rating': rating, 'poll': poll_pk, 'voter': voter}
        serializer = StateVoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class StateResultView(APIView):
    permission_classes=(IsAdminUser, IsAuthenticated,)
    def get(self, request):
        voter= request.user
        user = User.objects.get(username=voter)
        print(user.get_state)
        state=int(user.state.name)
        guber = Guber.objects.get(state=state)
        print(guber.governor.guber)
        #print(voter)
        votes = StateVote.objects.filter(state=state)
        print(votes)
        count_all = votes.count()
        count_0 = StateVote.objects.filter(state=state, rating=CHOICE[0][0]).count()
        count_1 = StateVote.objects.filter(state=state, rating=CHOICE[1][0]).count()
        count_2 = StateVote.objects.filter(state=state,rating=CHOICE[2][0]).count()
        count_3 = StateVote.objects.filter(state=state,rating=CHOICE[3][0]).count()
        count_4 = StateVote.objects.filter(state=state,rating=CHOICE[4][0]).count()
        count_5 = StateVote.objects.filter(state=state,rating=CHOICE[5][0]).count()
        
        vote_0 = int(count_0) * 0
        vote_1 = int(count_1) * 1
        vote_2 = int(count_2) * 2
        vote_3 = int(count_3) * 3
        vote_4 = int(count_4) * 4
        vote_5 = int(count_5) * 5
        
        vote_all= int(count_all) * 5
        
        # if count_all ==0:
        #     return f'No user has voted yet!!!'
        vote_total = vote_0 + vote_1 + vote_2 + vote_3 + vote_4  + vote_5
        # poll = FGPoll.objects.get(presidency=1)
        # party =int(poll.party.party.name)
        party =GuberParty.objects.get(state=user.state.id).party.party.get_party_name
        print(party)
        result= int((vote_total/vote_all)*100)
        data = {'state':user.get_state,'guber':{'governor':guber.governor.guber,'deputy_governor':guber.deputy_governor.guber, 'party':party},'result':f'{result}%','checker':user.get_full_name, 'date':datetime.datetime.now()
         }
        # print(data)
        # #print(result)
        return Response(data)

class Senatorial_districtPollViewset(viewsets.ModelViewSet):
    permission_classes=(IsAdminUser,)
    queryset= Senatorial_districtPoll.objects.all()
    serializer_class=Senatorial_districtPollSerializer

# class Senatorial_districtVoteViewset(viewsets.ModelViewSet):
#     queryset= Senatorial_districtVote.objects.all()
#     serializer_class=Senatorial_districtVoteSerializer

class Senatorial_DistrictCreateVote(APIView):
    permission_classes=(IsAdminUser, IsAuthenticated,)
    def post(self, request, poll_pk, rating):
        voter= request.user
        user = User.objects.get(username=voter)
        print(user.state.name)
        state=int(user.state.name)
        senate = Senate.objects.get(state=state)
        print(senate.senDis_id)
        poll = Senatorial_districtPoll.objects.get(pk=poll_pk)
        print(poll.manifestoe)
        print(poll.party.party.name)
        
        
        party = int(poll.party.party.name)
        data = {'state':state,'senDis':int(user.senDis_id),'party':party,'rating': rating, 'poll': poll_pk, 'voter': voter.id}
        print(data)
        serializer = Senatorial_districtVoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class Senatorial_districtResultView(APIView):
    permission_classes=(IsAdminUser, IsAuthenticated,)
    def get(self, request):
        voter= request.user
        user = User.objects.get(username=voter)
        #print(user.state.name)
        state=user.get_state
        senDis = user.senDis
        senate=Senate.objects.get(senDis=senDis.id)
        print(senate.senator.senate)
        print(senDis.id)
        votes = Senatorial_districtVote.objects.filter(senDis=senDis.id)
        print(votes)
        count_all = votes.count()
        count_0 = Senatorial_districtVote.objects.filter(senDis=senDis.id, rating=CHOICE[0][0]).count()
        count_1 = Senatorial_districtVote.objects.filter(senDis=senDis.id, rating=CHOICE[1][0]).count()
        count_2 = Senatorial_districtVote.objects.filter(senDis=senDis.id,rating=CHOICE[2][0]).count()
        count_3 = Senatorial_districtVote.objects.filter(senDis=senDis.id,rating=CHOICE[3][0]).count()
        count_4 = Senatorial_districtVote.objects.filter(senDis=senDis.id,rating=CHOICE[4][0]).count()
        count_5 = Senatorial_districtVote.objects.filter(senDis=senDis.id,rating=CHOICE[5][0]).count()
        
        vote_0 = int(count_0) * 0
        vote_1 = int(count_1) * 1
        vote_2 = int(count_2) * 2
        vote_3 = int(count_3) * 3
        vote_4 = int(count_4) * 4
        vote_5 = int(count_5) * 5
        
        vote_all= int(count_all) * 5
        
        # if count_all ==0:
        #     return f'No user has voted yet!!!'
        vote_total = vote_0 + vote_1 + vote_2 + vote_3 + vote_4  + vote_5
        # poll = FGPoll.objects.get(presidency=1)
        # party =int(poll.party.party.name)
        party=SenateParty.objects.get(senDis=user.senDis.id).party.get_party_name
        print(party)
        result= int((vote_total/vote_all)*100)
        data = {'state':state,'senatorial_district':senDis.get_senatorial_district_name,'senate':{'senator':senate.senator.senate,'party':party},'result':f'{result}%','checker':user.get_full_name, 'date':datetime.datetime.now()
         }
        # print(data)
        # #print(result)
        return Response(data)


class Federal_ConstituentPollViewset(viewsets.ModelViewSet):
    permission_classes=(IsAdminUser,)
    queryset= Federal_ConstituentPoll.objects.all()
    serializer_class=Federal_ConstituentPollSerializer

# class Federal_ConstituentVoteViewset(viewsets.ModelViewSet):
#     permission_classes=(IsAdminUser, IsAuthenticated,)
#     queryset= Federal_ConstituentVote.objects.all()
#     serializer_class=Federal_ConstituentVoteSerializer


class Federal_ConstituentCreateVote(APIView):
    permission_classes=(IsAdminUser, IsAuthenticated,)
    def post(self, request, poll_pk, rating):
        voter= request.user
        user = User.objects.get(username=voter)
        print(user.state.name)
        state=int(user.state.name)
        rep = Fed_Rep.objects.get(state=state)
        print(rep.fedCon.name)
        poll = Federal_ConstituentPoll.objects.get(pk=poll_pk)
        print(poll.manifestoe)
        print(poll.party.party.name)
        
        fedCon=int(rep.fedCon.name)
        
        party = int(poll.party.party.id)
        data = {'state':state,'fedCon':fedCon,'rating': rating, 'poll': poll_pk, 'voter': voter.id}
        print(data)
        serializer = Federal_ConstituentVoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class Federal_ConstituentResultView(APIView):
    permission_classes=(IsAdminUser, IsAuthenticated,)
    def get(self, request):
        voter= request.user
        user = User.objects.get(username=voter)
        #print(user.state.name)
        state=user.get_state
        fedCon = user.fedCon
        rep=Fed_Rep.objects.get(fedCon=fedCon.id)
        print(rep.rep.fed_reps)
        print(fedCon.id)
        votes = Federal_ConstituentVote.objects.filter(fedCon=fedCon.id)
        print(votes)
        count_all = votes.count()
        count_0 = Federal_ConstituentVote.objects.filter(fedCon=fedCon.id, rating=CHOICE[0][0]).count()
        count_1 = Federal_ConstituentVote.objects.filter(fedCon=fedCon.id, rating=CHOICE[1][0]).count()
        count_2 = Federal_ConstituentVote.objects.filter(fedCon=fedCon.id,rating=CHOICE[2][0]).count()
        count_3 = Federal_ConstituentVote.objects.filter(fedCon=fedCon.id,rating=CHOICE[3][0]).count()
        count_4 = Federal_ConstituentVote.objects.filter(fedCon=fedCon.id,rating=CHOICE[4][0]).count()
        count_5 = Federal_ConstituentVote.objects.filter(fedCon=fedCon.id,rating=CHOICE[5][0]).count()
        
        vote_0 = int(count_0) * 0
        vote_1 = int(count_1) * 1
        vote_2 = int(count_2) * 2
        vote_3 = int(count_3) * 3
        vote_4 = int(count_4) * 4
        vote_5 = int(count_5) * 5
        
        vote_all= int(count_all) * 5
        
        # if count_all ==0:
        #     return f'No user has voted yet!!!'
        vote_total = vote_0 + vote_1 + vote_2 + vote_3 + vote_4  + vote_5
        # poll = FGPoll.objects.get(presidency=1)
        # party =int(poll.party.party.name)
        party=Fed_RepParty.objects.get(fedCon=user.fedCon.id).party.get_party_name
        print(party)
        result= int((vote_total/vote_all)*100)
        data = {'state':state,'federal_constuency':fedCon.get_fed_con_name,'representative':{'rep':rep.rep.fed_reps,'party':party},'result':f'{result}%','checker':user.get_full_name, 'date':datetime.datetime.now()
         }
        # print(data)
        # #print(result)
        return Response(data)



class LGAPollViewset(viewsets.ModelViewSet):
    permission_classes=(IsAdminUser,)
    queryset= LGAPoll.objects.all()
    serializer_class=LGAPollSerializer

class LGACreateVote(APIView):
    permission_classes=(IsAdminUser, IsAuthenticated,)
    def post(self, request, poll_pk, rating):
        voter= request.user
        user = User.objects.get(username=voter)
        print(user.state.name)
        state=int(user.state.name)
        chairmanship = Chairmanship.objects.get(state=state)
        poll = LGAPoll.objects.get(pk=poll_pk)
        print(poll.manifestoe)
        print(poll.party.party.name)
        
        lga=int(chairmanship.lga.name)
        
        party = int(poll.party.party.id)
        data = {'state':state,'lga':user.lga.id,'rating': rating, 'poll': poll_pk, 'voter': voter.id}
        print(data)
        serializer = LGAVoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class LGAResultView(APIView):
    permission_classes=(IsAdminUser, IsAuthenticated,)
    def get(self, request):
        voter= request.user
        user = User.objects.get(username=voter)
        print(user.state.name)
        state=user.get_state
        lga = user.lga
        chairmanship=Chairmanship.objects.get(lga=lga.id)
        print(chairmanship)
        print(lga.id)
        votes = LGAVote.objects.filter(lga=lga.id)
        print(votes)
        count_all = votes.count()
        count_0 = LGAVote.objects.filter(lga=lga.id, rating=CHOICE[0][0]).count()
        count_1 = LGAVote.objects.filter(lga=lga.id, rating=CHOICE[1][0]).count()
        count_2 = LGAVote.objects.filter(lga=lga.id,rating=CHOICE[2][0]).count()
        count_3 = LGAVote.objects.filter(lga=lga.id,rating=CHOICE[3][0]).count()
        count_4 = LGAVote.objects.filter(lga=lga.id,rating=CHOICE[4][0]).count()
        count_5 = LGAVote.objects.filter(lga=lga.id,rating=CHOICE[5][0]).count()
        
        vote_0 = int(count_0) * 0
        vote_1 = int(count_1) * 1
        vote_2 = int(count_2) * 2
        vote_3 = int(count_3) * 3
        vote_4 = int(count_4) * 4
        vote_5 = int(count_5) * 5
        
        vote_all= int(count_all) * 5
        
        # if count_all ==0:
        #     return f'No user has voted yet!!!'
        vote_total = vote_0 + vote_1 + vote_2 + vote_3 + vote_4  + vote_5
        # poll = FGPoll.objects.get(presidency=1)
        # party =int(poll.party.party.name)
        chairman=chairmanship.chairman.chairmanship
        vice_chairman=chairmanship.vice_chairman.chairmanship
        party=ChairmanshipParty.objects.get(lga=user.lga.id)
        result= int((vote_total/vote_all)*100)
        data = {'state':state,'lga':lga.get_lga_name,'chairmanship':{'chairman':chairman,'vice_chairman':vice_chairman,'party':party.party.get_party_name},'result':f'{result}%','checker':user.get_full_name, 'date':datetime.datetime.now()
         }
        # print(data)
        # #print(result)
        return Response(data)




class State_ConstituentPollViewset(viewsets.ModelViewSet):
    queryset= State_ConstituentPoll.objects.all()
    serializer_class=State_ConstituentPollSerializer

class State_ConstituentCreateVote(APIView):
    permission_classes=(IsAdminUser, IsAuthenticated,)
    def post(self, request, poll_pk, rating):
        voter= request.user
        user = User.objects.get(username=voter)
        print(user.state.name)
        state=int(user.state.name)
        state_rep = State_Rep.objects.get(stateCon=user.state_con.id)
        poll = State_ConstituentPoll.objects.get(pk=poll_pk)
        # print(poll.manifestoe)
        print(poll.party.party.name)
        
        stateCon=int(state_rep.stateCon.name)
        
        party = int(poll.party.party.id)
        data = {'state':state,'lga':user.lga.id,'stateCon':user.state_con.id,'rating': rating, 'poll': poll_pk, 'voter': voter.id}
        # print(state_rep)
        serializer = State_ConstituentVoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class State_ConstituentResultView(APIView):
    permission_classes=(IsAdminUser, IsAuthenticated,)
    def get(self, request):
        voter= request.user
        user = User.objects.get(username=voter)
        #print(user.state.name)
        state=user.get_state
        stateCon= user.state_con
        rep=State_Rep.objects.get(stateCon=stateCon.id)
        print(rep)
        print(stateCon.id)
        votes = State_ConstituentVote.objects.filter(stateCon=stateCon.id)
        print(votes)
        count_all = votes.count()
        count_0 = State_ConstituentVote.objects.filter(stateCon=stateCon.id, rating=CHOICE[0][0]).count()
        count_1 = State_ConstituentVote.objects.filter(stateCon=stateCon.id, rating=CHOICE[1][0]).count()
        count_2 = State_ConstituentVote.objects.filter(stateCon=stateCon.id,rating=CHOICE[2][0]).count()
        count_3 = State_ConstituentVote.objects.filter(stateCon=stateCon.id,rating=CHOICE[3][0]).count()
        count_4 = State_ConstituentVote.objects.filter(stateCon=stateCon.id,rating=CHOICE[4][0]).count()
        count_5 = State_ConstituentVote.objects.filter(stateCon=stateCon.id,rating=CHOICE[5][0]).count()
        
        vote_0 = int(count_0) * 0
        vote_1 = int(count_1) * 1
        vote_2 = int(count_2) * 2
        vote_3 = int(count_3) * 3
        vote_4 = int(count_4) * 4
        vote_5 = int(count_5) * 5
        
        vote_all= int(count_all) * 5
        
        # if count_all ==0:
        #     return f'No user has voted yet!!!'
        vote_total = vote_0 + vote_1 + vote_2 + vote_3 + vote_4  + vote_5
        # poll = FGPoll.objects.get(presidency=1)
        # party =int(poll.party.party.name)
        # rep=rep.rep.state_reps
        rep=rep.rep.state_reps
        
        # vice_chairman=chairmanship.vice_chairman.chairmanship
        party=State_RepParty.objects.get(stateCon=user.state_con.id)
        result= int((vote_total/vote_all)*100)
        data = {'state':state,'lga':user.lga.get_lga_name,'state_rep':{'rep':rep,'party':party.party.get_party_name},'result':f'{result}%','checker':user.get_full_name, 'date':datetime.datetime.now()
          }
        # # print(data)
        # #print(result)
        return Response(data)


class WardPollViewset(viewsets.ModelViewSet):
    queryset= WardPoll.objects.all()
    serializer_class=WardPollSerializer


class WardCreateVote(APIView):
    permission_classes=(IsAdminUser, IsAuthenticated,)
    def post(self, request, poll_pk, rating):
        voter= request.user
        user = User.objects.get(username=voter)
        print(user.state.name)
        # ward=int(user.ward.name)
        councilorship = Councilorship.objects.get(ward=user.ward)
        poll = WardPoll.objects.get(pk=poll_pk)
        # print(poll.manifestoe)
        print(poll.party.party.name)
        
        # ward=int(councilorship.ward.name)
        print(user.ward.name)
        party = int(poll.party.party.id)
        data = {'state':user.state,'lga':user.lga.id,'stateCon':user.state_con.id, 'ward':user.ward.id,'rating': rating, 'poll': poll_pk, 'voter': voter.id}
        # print(state_rep)
        serializer = WardVoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class WardResultView(APIView):
    permission_classes=(IsAdminUser, IsAuthenticated,)
    def get(self, request):
        voter= request.user
        user = User.objects.get(username=voter)
        #print(user.state.name)
        state=user.get_state
        stateCon= user.state_con
        ward=user.ward
        councilor=Councilorship.objects.get(ward=ward)
        print(councilor)
        print(stateCon.id)
        votes = WardVote.objects.filter(ward=ward.id)
        print(votes)
        count_all = votes.count()
        count_0 = WardVote.objects.filter(ward=ward.id, rating=CHOICE[0][0]).count()
        count_1 = WardVote.objects.filter(ward=ward.id, rating=CHOICE[1][0]).count()
        count_2 = WardVote.objects.filter(ward=ward.id,rating=CHOICE[2][0]).count()
        count_3 = WardVote.objects.filter(ward=ward.id,rating=CHOICE[3][0]).count()
        count_4 = WardVote.objects.filter(ward=ward.id,rating=CHOICE[4][0]).count()
        count_5 = WardVote.objects.filter(ward=ward.id,rating=CHOICE[5][0]).count()
        
        vote_0 = int(count_0) * 0
        vote_1 = int(count_1) * 1
        vote_2 = int(count_2) * 2
        vote_3 = int(count_3) * 3
        vote_4 = int(count_4) * 4
        vote_5 = int(count_5) * 5
        
        vote_all= int(count_all) * 5
        
        # if count_all ==0:
        #     return f'No user has voted yet!!!'
        vote_total = vote_0 + vote_1 + vote_2 + vote_3 + vote_4  + vote_5
        # poll = FGPoll.objects.get(presidency=1)
        # party =int(poll.party.party.name)
        # rep=rep.rep.state_reps
        councilor=councilor.councilor.councilorship
        print(councilor)
        
        # vice_chairman=chairmanship.vice_chairman.chairmanship
        party=State_RepParty.objects.get(stateCon=user.state_con.id)
        result= int((vote_total/vote_all)*100)
        data = {'state':state,'lga':user.lga.get_lga_name,'ward':ward.name,'councilorship':{'councilor':councilor,'party':party.party.get_party_name},'result':f'{result}%','checker':user.get_full_name, 'date':datetime.datetime.now()
          }
        # # print(data)
        # #print(result)
        return Response(data)



