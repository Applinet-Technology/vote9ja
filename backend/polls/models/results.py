
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



class Result(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='voter_user_result', blank=True, null=True)
    result_checked_date = models.DateTimeField(auto_now=True)
    no_vote = 'No vote yet by vote9ja users in '
    
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
        
        
        # if federal_total_vote ==0:
        #     return f'No user has voted yet!!!'
        vote_total = vote_0 + vote_1 + vote_2 + vote_3 + vote_4  + vote_5
        
        result= int((vote_total/vote_all)*100)
        
        print(f'votes 0 {count_0} voters = {vote_0}')
        print(f'votes 1 {count_1} voters = {vote_1}')
        print(f'votes 2 {count_2} voters = {vote_2}')
        print(f'votes 3 {count_3} voters = {vote_3}')
        print(f'votes 4 {count_4} voters = {vote_4}')
        print(f'votes 5 {count_5} voters = {vote_5}')
        print(f'votes all {count_all} voters =  {vote_all}')
        print(f'FG ({result}%)')
        return f'FG ({result}%)'
    
    @property
    def state_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
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
        
        vote_total = vote_0 + vote_1 + vote_2 + vote_3 + vote_4  + vote_5
        result= int((vote_total/vote_all)*100)
        
        print(f'votes 0 {count_0} voters = {vote_0}')
        print(f'votes 1 {count_1} voters = {vote_1}')
        print(f'votes 2 {count_2} voters = {vote_2}')
        print(f'votes 3 {count_3} voters = {vote_3}')
        print(f'votes 4 {count_4} voters = {vote_4}')
        print(f'votes 5 {count_5} voters = {vote_5}')
        print(f'votes all {count_all} voters =  {vote_all}')
        print(f'FG ({result}%)')

        #state_count = count_yes.filter(state=voter.state).count()
        # if state_total_vote ==0:
        #     return f'{self.no_vote} {voter.state} State!!!'
        # result = int((state_count/state_total_vote)*100)
        # return f'{voter.state} State ({result}%)'
    
    
    @property
    def senatorial_district_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        #sed = Senatorial_district.objects.filter(name=voter.senDis)
        sendist = Senatorial_districtVote.objects.filter(senatorial_district=voter.senDis).count()
        print(sendist)
        sendist_total_vote = sendist
        print(sendist_total_vote)
        count_yes = Senatorial_districtVote.objects.filter(choice=CHOICE[0][0])
        sendist_count = count_yes.filter(senatorial_district=voter.senDis).count()
        if sendist_total_vote ==0:
            return f'{self.no_vote} {self.voter.senDis} Senatorial District!!!'
        result = int((sendist_count/sendist_total_vote)*100)
        return f'{self.voter.senDis} Senatorial District ({result}%)'
    
    @property
    def federal_constituency_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        #sed = Senatorial_district.objects.filter(name=voter.senDis)
        federal_constituency_counted = Federal_ConstituentVote.objects.filter(federal_constituency=voter.fedCon).count()
        #print(sendist)
        fedconst_total_vote = federal_constituency_counted
        #print(fedconst_total_vote)
        count_yes = Federal_ConstituentVote.objects.filter(choice=CHOICE[0][0])
        fedconst_count = count_yes.filter(federal_constituency=voter.fedCon).count()
        if fedconst_total_vote ==0:
            return f'{self.no_vote} {self.voter.fedCon} Federal Constituency!!!'
        result = int((fedconst_count/fedconst_total_vote)*100)
        return f'{self.voter.fedCon} Federal Constituency ({result}%)'

    @property
    def lga_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        voter_lga=voter.lga
        lga_total_vote = LGAVote.objects.filter(lga=voter_lga).count()
        count_yes = LGAVote.objects.filter(choice=CHOICE[0][0])
        lga_count = count_yes.filter(lga=voter_lga).count()
        if lga_total_vote ==0:
            return f'{self.no_vote} {voter_lga} LGA'
        result = int((lga_count/lga_total_vote)*100)
        return f'{voter_lga} LGA ({result}%)'
        
        
    @property
    def state_constituency_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        voter_state_con=voter.state_con
        state_con_total_vote = State_ConstituentVote.objects.filter(state_con=voter_state_con).count()
        count_yes = State_ConstituentVote.objects.filter(choice=CHOICE[0][0])
        state_con_count = count_yes.filter(state_con=voter_state_con).count()
        if state_con_total_vote ==0:
            return f'{self.no_vote} {voter_state_con} State Constituency'
        result = int((state_con_count/state_con_total_vote)*100)
        return f'{voter_state_con} State Constituency ({result}%)'
    
    
    
    @property
    def ward_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        voter_ward=voter.ward
        ward_total_vote = WardVote.objects.filter(ward=voter_ward).count()
        count_yes = WardVote.objects.filter(choice=CHOICE[0][0])
        ward_count = count_yes.filter(ward=voter_ward).count()
        if ward_total_vote ==0:
            return f'{self.no_vote} {voter_ward} Ward'
        result = int((ward_count/ward_total_vote)*100)
        return f'{voter_ward} Ward ({result}%)'
    
    
    def __str__(self):
        return f'{self.voter} ...checking Performance  Scores: Federal ({self.federal_vote_count}) ({self.state_vote_count}) ({self.senatorial_district_vote_count}) ({self.federal_constituency_vote_count}) ({self.lga_vote_count}) ({self.state_constituency_vote_count}) ({self.ward_vote_count}) >>>>Last Result request date: {self.result_checked_date}'