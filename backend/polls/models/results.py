
from django.db import models
from accounts.models.users import User
from .state_constituencypolls import State_ConstituentVote
from .federalpolls import FGVote
from .statepolls import StateVote
from .senatorial_districtpolls import Senatorial_districtVote
from .federal_constituencypolls import Federal_ConstituentVote
from .lgapolls import LGAVote
from .wardpolls import WardVote
from .polls import CHOICE
from politicians.models import PoliticalParty, PresidencyParty, GuberParty, Guber, GParty



class Result(models.Model):
    party = models.ForeignKey(GParty, on_delete=models.CASCADE, default=1)
    
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='voter_user_result', blank=True, null=True)
    result_checked_date = models.DateTimeField(auto_now=True)
    no_vote = 'No vote yet by vote9ja users in '
    
    @property
    def partyOverallRating(self):
        # party = PresidencyParty.objects.get(presidency=1)
        # fg_count_all = FGVote.objects.filter(party=party).count()
        
        # fgcount_0 = FGVote.objects.filter(party=party, rating=CHOICE[0][0]).count()
        # fgcount_1 = FGVote.objects.filter(party=party, rating=CHOICE[1][0]).count()
        # fgcount_2 = FGVote.objects.filter(party=party,rating=CHOICE[2][0]).count()
        # fgcount_3 = FGVote.objects.filter(party=party,rating=CHOICE[3][0]).count()
        # fgcount_4 = FGVote.objects.filter(party=party,rating=CHOICE[4][0]).count()
        # fgcount_5 = FGVote.objects.filter(party=party,rating=CHOICE[5][0]).count()
        
        # fgvote_0 = int(fgcount_0) * 0
        # fgvote_1 = int(fgcount_1) * 1
        # fgvote_2 = int(fgcount_2) * 2
        # fgvote_3 = int(fgcount_3) * 3
        # fgvote_4 = int(fgcount_4) * 4
        # fgvote_5 = int(fgcount_5) * 5
        # fgvote_total = fgvote_0 + fgvote_1 + fgvote_2 + fgvote_3 + fgvote_4  + fgvote_5
        
        
        
        # print(f'FEDERAL Party RATING {party} {fgvote_total}')
        # prty=Guber.objects.get(state=self.party)
        
        vt = StateVote.objects.all()
        gParty = GuberParty.objects.get(party=self.party)

        print(f"guber{gParty}")
        

    
    
    
    @property
    def federal_vote_count(self):
        count_all = FGVote.objects.all().count()
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
        
        result= int((vote_total/vote_all)*100)
        
        # print(f'votes 0 {count_0} voters = {vote_0}')
        # print(f'votes 1 {count_1} voters = {vote_1}')
        # print(f'votes 2 {count_2} voters = {vote_2}')
        # print(f'votes 3 {count_3} voters = {vote_3}')
        # print(f'votes 4 {count_4} voters = {vote_4}')
        # print(f'votes 5 {count_5} voters = {vote_5}')
        # print(f'votes all {count_all} voters =  {vote_all}')
        # print(f'FG ({result}%)')
        return f'Federal Government of Nigeria Performance Rating: ({result}%)'
    
    @property
    def state_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        print(self.voter)
        count_all = StateVote.objects.filter(state=voter.state).count()
        count_0 = StateVote.objects.filter(state=voter.state, rating=CHOICE[0][0]).count()
        count_1 = StateVote.objects.filter(state=voter.state, rating=CHOICE[1][0]).count()
        count_2 = StateVote.objects.filter(state=voter.state, rating=CHOICE[2][0]).count()
        count_3 = StateVote.objects.filter(state=voter.state, rating=CHOICE[3][0]).count()
        count_4 = StateVote.objects.filter(state=voter.state, rating=CHOICE[4][0]).count()
        count_5 = StateVote.objects.filter(state=voter.state, rating=CHOICE[5][0]).count()
        
        vote_0 = int(count_0) * 0
        vote_1 = int(count_1) * 1
        vote_2 = int(count_2) * 2
        vote_3 = int(count_3) * 3
        vote_4 = int(count_4) * 4
        vote_5 = int(count_5) * 5
        vote_all= int(count_all) * 5
        
        if count_all ==0:
            return f'{self.no_vote} {voter.state} State!!!'
        vote_total = vote_0 + vote_1 + vote_2 + vote_3 + vote_4  + vote_5
        
        result= int((vote_total/vote_all)*100)
        
        # print(f'votes 0 {count_0} voters = {vote_0}')
        # print(f'votes 1 {count_1} voters = {vote_1}')
        # print(f'votes 2 {count_2} voters = {vote_2}')
        # print(f'votes 3 {count_3} voters = {vote_3}')
        # print(f'votes 4 {count_4} voters = {vote_4}')
        # print(f'votes 5 {count_5} voters = {vote_5}')
        # print(f'votes all {count_all} voters =  {vote_all}')
        # print(f'{voter.state} State Government Performance Rating: ({result}%)')
        
        return f'{voter.state} State Government Performance Rating ({result}%)'
    
    
    @property
    def senatorial_district_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        count_all = Senatorial_districtVote.objects.filter(senDis=voter.senDis).count()
        count_0 = Senatorial_districtVote.objects.filter(senDis=voter.senDis, rating=CHOICE[0][0]).count()
        count_1 = Senatorial_districtVote.objects.filter(senDis=voter.senDis, rating=CHOICE[1][0]).count()
        count_2 = Senatorial_districtVote.objects.filter(senDis=voter.senDis, rating=CHOICE[2][0]).count()
        count_3 = Senatorial_districtVote.objects.filter(senDis=voter.senDis, rating=CHOICE[3][0]).count()
        count_4 = Senatorial_districtVote.objects.filter(senDis=voter.senDis, rating=CHOICE[4][0]).count()
        count_5 = Senatorial_districtVote.objects.filter(senDis=voter.senDis, rating=CHOICE[5][0]).count()
        
        vote_0 = int(count_0) * 0
        vote_1 = int(count_1) * 1
        vote_2 = int(count_2) * 2
        vote_3 = int(count_3) * 3
        vote_4 = int(count_4) * 4
        vote_5 = int(count_5) * 5
        vote_all= int(count_all) * 5
        
        
        vote_total = vote_0 + vote_1 + vote_2 + vote_3 + vote_4  + vote_5
        if count_all ==0:
            return self.no_vote

        result= int((vote_total/vote_all)*100)
        
        # print(f'votes 0 {count_0} voters = {vote_0}')
        # print(f'votes 1 {count_1} voters = {vote_1}')
        # print(f'votes 2 {count_2} voters = {vote_2}')
        # print(f'votes 3 {count_3} voters = {vote_3}')
        # print(f'votes 4 {count_4} voters = {vote_4}')
        # print(f'votes 5 {count_5} voters = {vote_5}')
        # print(f'votes all {count_all} voters =  {vote_all}')
        return f'{self.voter.senDis} Senatorial District Performance Rating: ({result}%)'

    @property
    def federal_constituency_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        count_all = Federal_ConstituentVote.objects.filter(fedCon=voter.fedCon).count()
        count_0 = Federal_ConstituentVote.objects.filter(fedCon=voter.fedCon, rating=CHOICE[0][0]).count()
        count_1 = Federal_ConstituentVote.objects.filter(fedCon=voter.fedCon, rating=CHOICE[1][0]).count()
        count_2 = Federal_ConstituentVote.objects.filter(fedCon=voter.fedCon, rating=CHOICE[2][0]).count()
        count_3 = Federal_ConstituentVote.objects.filter(fedCon=voter.fedCon, rating=CHOICE[3][0]).count()
        count_4 = Federal_ConstituentVote.objects.filter(fedCon=voter.fedCon, rating=CHOICE[4][0]).count()
        count_5 = Federal_ConstituentVote.objects.filter(fedCon=voter.fedCon, rating=CHOICE[5][0]).count()
        
        vote_0 = int(count_0) * 0
        vote_1 = int(count_1) * 1
        vote_2 = int(count_2) * 2
        vote_3 = int(count_3) * 3
        vote_4 = int(count_4) * 4
        vote_5 = int(count_5) * 5
        vote_all= int(count_all) * 5
        
        vote_total = vote_0 + vote_1 + vote_2 + vote_3 + vote_4  + vote_5
        if count_all ==0:
            return self.no_vote
        result= int((vote_total/vote_all)*100)
        
        # print(f'votes 0 {count_0} voters = {vote_0}')
        # print(f'votes 1 {count_1} voters = {vote_1}')
        # print(f'votes 2 {count_2} voters = {vote_2}')
        # print(f'votes 3 {count_3} voters = {vote_3}')
        # print(f'votes 4 {count_4} voters = {vote_4}')
        # print(f'votes 5 {count_5} voters = {vote_5}')
        # print(f'votes all {count_all} voters =  {vote_all}')
        return f'{self.voter.fedCon} Federal Constituency Performance Rating: ({result}%)'

    @property
    def lga_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        count_all = LGAVote.objects.filter(lga=voter.lga).count()
        count_0 = LGAVote.objects.filter(lga=voter.lga, rating=CHOICE[0][0]).count()
        count_1 = LGAVote.objects.filter(lga=voter.lga, rating=CHOICE[1][0]).count()
        count_2 = LGAVote.objects.filter(lga=voter.lga, rating=CHOICE[2][0]).count()
        count_3 = LGAVote.objects.filter(lga=voter.lga, rating=CHOICE[3][0]).count()
        count_4 = LGAVote.objects.filter(lga=voter.lga, rating=CHOICE[4][0]).count()
        count_5 = LGAVote.objects.filter(lga=voter.lga, rating=CHOICE[5][0]).count()
        
        vote_0 = int(count_0) * 0
        vote_1 = int(count_1) * 1
        vote_2 = int(count_2) * 2
        vote_3 = int(count_3) * 3
        vote_4 = int(count_4) * 4
        vote_5 = int(count_5) * 5
        vote_all= int(count_all) * 5
        
        vote_total = vote_0 + vote_1 + vote_2 + vote_3 + vote_4  + vote_5
        if count_all ==0:
            return self.no_vote
        result= int((vote_total/vote_all)*100)
        
        # print(f'votes 0 {count_0} voters = {vote_0}')
        # print(f'votes 1 {count_1} voters = {vote_1}')
        # print(f'votes 2 {count_2} voters = {vote_2}')
        # print(f'votes 3 {count_3} voters = {vote_3}')
        # print(f'votes 4 {count_4} voters = {vote_4}')
        # print(f'votes 5 {count_5} voters = {vote_5}')
        # print(f'votes all {count_all} voters =  {vote_all}')
        # print(f'lga ({result}%)')
        return f'{self.voter.lga} Local Government Performance Rating {result}%'
        
    @property
    def state_constituency_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        count_all = State_ConstituentVote.objects.filter(stateCon=voter.state_con).count()
        count_0 = State_ConstituentVote.objects.filter(stateCon=voter.state_con, rating=CHOICE[0][0]).count()
        count_1 = State_ConstituentVote.objects.filter(stateCon=voter.state_con, rating=CHOICE[1][0]).count()
        count_2 = State_ConstituentVote.objects.filter(stateCon=voter.state_con, rating=CHOICE[2][0]).count()
        count_3 = State_ConstituentVote.objects.filter(stateCon=voter.state_con, rating=CHOICE[3][0]).count()
        count_4 = State_ConstituentVote.objects.filter(stateCon=voter.state_con, rating=CHOICE[4][0]).count()
        count_5 = State_ConstituentVote.objects.filter(stateCon=voter.state_con, rating=CHOICE[5][0]).count()
        
        vote_0 = int(count_0) * 0
        vote_1 = int(count_1) * 1
        vote_2 = int(count_2) * 2
        vote_3 = int(count_3) * 3
        vote_4 = int(count_4) * 4
        vote_5 = int(count_5) * 5
        vote_all= int(count_all) * 5
        
        vote_total = vote_0 + vote_1 + vote_2 + vote_3 + vote_4  + vote_5
        if count_all ==0:
            return self.no_vote
        result= int((vote_total/vote_all)*100)
        
        # print(f'votes 0 {count_0} voters = {vote_0}')
        # print(f'votes 1 {count_1} voters = {vote_1}')
        # print(f'votes 2 {count_2} voters = {vote_2}')
        # print(f'votes 3 {count_3} voters = {vote_3}')
        # print(f'votes 4 {count_4} voters = {vote_4}')
        # print(f'votes 5 {count_5} voters = {vote_5}')
        # print(f'votes all {count_all} voters =  {vote_all}')
        # print(f'{voter.state_con} State Cobstituency Performance Rating ({result}%)')
        
        return f'{voter.state_con} State Constituency ({result}%)'
    
    
    
    @property
    def ward_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        count_all = WardVote.objects.filter(ward=voter.ward).count()
        count_0 = WardVote.objects.filter(ward=voter.ward, rating=CHOICE[0][0]).count()
        count_1 = WardVote.objects.filter(ward=voter.ward, rating=CHOICE[1][0]).count()
        count_2 = WardVote.objects.filter(ward=voter.ward, rating=CHOICE[2][0]).count()
        count_3 = WardVote.objects.filter(ward=voter.ward, rating=CHOICE[3][0]).count()
        count_4 = WardVote.objects.filter(ward=voter.ward, rating=CHOICE[4][0]).count()
        count_5 = WardVote.objects.filter(ward=voter.ward, rating=CHOICE[5][0]).count()
        
        vote_0 = int(count_0) * 0
        vote_1 = int(count_1) * 1
        vote_2 = int(count_2) * 2
        vote_3 = int(count_3) * 3
        vote_4 = int(count_4) * 4
        vote_5 = int(count_5) * 5
        vote_all= int(count_all) * 5
        
        vote_total = vote_0 + vote_1 + vote_2 + vote_3 + vote_4  + vote_5
        if count_all ==0:
            return self.no_vote
        result= int((vote_total/vote_all)*100)
        
        # print(f'votes 0 {count_0} voters = {vote_0}')
        # print(f'votes 1 {count_1} voters = {vote_1}')
        # print(f'votes 2 {count_2} voters = {vote_2}')
        # print(f'votes 3 {count_3} voters = {vote_3}')
        # print(f'votes 4 {count_4} voters = {vote_4}')
        # print(f'votes 5 {count_5} voters = {vote_5}')
        # print(f'votes all {count_all} voters =  {vote_all}')
        # print(f'Ward ({result}%)')
    
        return f'{voter.ward} Ward Performance Rating: ({result}%)'
    
    def __str__(self):
         return f'{self.voter} ...checking Performance  Scores: Federal ({self.federal_vote_count}) ({self.state_vote_count}) ({self.senatorial_district_vote_count}) ({self.federal_constituency_vote_count}) ({self.lga_vote_count}) ({self.state_constituency_vote_count}) ({self.ward_vote_count}) Party rating {self.partyOverallRating}>>>>Last Result request date: {self.result_checked_date}'