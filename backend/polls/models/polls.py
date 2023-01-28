

import datetime
from django.db import models
from accounts.models.users import User
from smart_selects.db_fields import ChainedForeignKey
from accounts.models.federal import Federal
from accounts.models.states import State
from accounts.models.senatorial_districts import Senatorial_district
from accounts.models.federal_constituencies import Federal_Constituent
from accounts.models.lgas import LGA
from accounts.models.wards import Ward


class Sector(models.Model):
    name = models.CharField(max_length=50, default='Sector', unique=True)
    
    def __str__(self):
        return self.name

class Manifestoe(models.Model):
    sector = models.OneToOneField(Sector, on_delete=models.CASCADE, related_name='manifestoe_sector')
    manifestoe_title = models.CharField(max_length=50, unique=True)
    manifestoe = models.TextField(unique=True)
    def __str__(self):
        return f'{self.sector}: {self.manifestoe}'

class Poll(models.Model):
    manifestoe = models.OneToOneField(Manifestoe, on_delete=models.CASCADE, related_name='manifestoe_poll', unique_for_date='activation_date', default=1)
    activation_date = models.DateTimeField(auto_now=True)
    expiry_date = models.DateTimeField()
    
    @property
    def poll_is_active(self):
        #poll=Poll.objects.get(id=self.poll_id)
        expiry =self.expiry_date.date()
        current=datetime.date.today()
        if current<expiry:
            return True
            #f'{self.manifestoe} Poll with expiry date {expiry} has expired' 
        return False
        #f'{self.manifestoe} Poll with expiry date {expiry} is active'
        # print(f'active >>> {current>expiry}')
        # print(f'active>>> {current<=expiry}')
        
    def save(self, *args, **kwargs):
        if datetime.date.today() > self.expiry_date.date():
            print('Expiry date is invalid!')
            return 'Expiry date is invalid!'
        super().save(self, *args, **kwargs)
    
    def __str__(self):
        return f'{self.manifestoe.manifestoe}'
        
        
        
CHOICE = (('yes','Done'),('no','Undone'))

class FederalPoll(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='federal_voter', default=2)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='federal_poll', default=1)
    choice = models.CharField(max_length=10, choices=CHOICE)
    vote_date = models.DateTimeField(auto_now_add=True)
    has_voted = models.BooleanField(default=True)
        
    
    def save(self, *args, **kwargs):
        #voter = User.objects.get(id = self.voter_id)
        poll=Poll.objects.get(id=self.poll_id)
        poll_is_active=self.poll.poll_is_active
        if poll_is_active != True:                print('Poll no longer active.')
        print(poll.expiry_date)
        #super().save(self, *args, **kwargs)
            
    
    def __str__(self):
        return f'{self.poll.manifestoe.sector} performance poll on {self.vote_date}'

class StatePoll(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='state_voter')
    state= ChainedForeignKey(State,
        chained_field="voter",
        chained_model_field="user_state",
        show_all=False, 
        auto_choose=True,
        sort=True
        )
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='state_poll', default=1)
    choice = models.CharField(max_length=10, choices=CHOICE)
    vote_date = models.DateTimeField(auto_now=True)
    has_voted = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        poll=Poll.objects.get(id=self.poll_id)
        poll_is_active=self.poll.poll_is_active
        if poll_is_active != True:
            return 'Poll no longer active.'
        print(poll.expiry_date)
        super().save(self, *args, **kwargs)
    
    def __str__(self):
        return f'{self.poll.manifestoe.sector} {self.state} State performance poll on {self.vote_date}'

class Senatorial_districtPoll(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='senatorial_district_voter')
    
    senatorial_district= ChainedForeignKey(Senatorial_district,
        chained_field="voter",
        chained_model_field="user",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='senatorial_district_poll', default=1)
    choice = models.CharField(max_length=10, choices=CHOICE)
    vote_date = models.DateTimeField(auto_now=True)
    has_voted = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        poll=Poll.objects.get(id=self.poll_id)
        poll_is_active=self.poll.poll_is_active
        if poll_is_active != True:
            return 'Poll no longer active.'
        print(poll.expiry_date)
        super().save(self, *args, **kwargs)
    
    def __str__(self):
        return f'{self.poll.manifestoe.sector} {self.senatorial_district}'
        
class Federal_ConstituentPoll(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='federal_constituent_voter', default=2)
    
    federal_constituency= ChainedForeignKey(Federal_Constituent,
        chained_field="voter",
        chained_model_field="user",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='federal_constituency_poll', default=1)
    choice = models.CharField(max_length=10, choices=CHOICE)
    
    def save(self, *args, **kwargs):
        poll=Poll.objects.get(id=self.poll_id)
        poll_is_active=self.poll.poll_is_active
        if poll_is_active != True:
            return 'Poll no longer active.'
        print(poll.expiry_date)
        super().save(self, *args, **kwargs)
    
    vote_date = models.DateTimeField(auto_now=True)
    has_voted = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.poll.manifestoe.sector} {self.federal_constituency}'
   
class LGAPoll(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='lga_voter')
    lga= ChainedForeignKey(LGA,
        chained_field="voter",
        chained_model_field="user",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='lga_poll', default=1)
    choice = models.CharField(max_length=10, choices=CHOICE)
    vote_date = models.DateTimeField(auto_now=True)
    has_voted = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        poll=Poll.objects.get(id=self.poll_id)
        poll_is_active=self.poll.poll_is_active
        if poll_is_active != True:
            return 'Poll no longer active.'
        print(poll.expiry_date)
        super().save(self, *args, **kwargs)
    
    def __str__(self):
        return f'{self.voter} has voted on {self.poll.manifestoe.sector} {self.voter.lga} LGA performance poll on {self.vote_date}'

   
class WardPoll(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='ward_voter', default=1)
    ward= ChainedForeignKey(Ward,
        chained_field="voter",
        chained_model_field="user",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='ward_poll', default=1)
    choice = models.CharField(max_length=10, choices=CHOICE)
    vote_date = models.DateTimeField(auto_now=True)
    has_voted = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        poll=Poll.objects.get(id=self.poll_id)
        poll_is_active=self.poll.poll_is_active
        if poll_is_active != True:
            return 'Poll no longer active.'
        print(poll.expiry_date)
        super().save(self, *args, **kwargs)
    
    def __str__(self):
        return f'{self.voter} has voted on {self.poll.manifestoe.sector} {self.voter.ward} Ward performance poll on {self.vote_date}'


class Result(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='voter_user_result', blank=True, null=True)
    result_checked_date = models.DateTimeField(auto_now=True)
    no_vote = 'No vote yet by vote9ja users in '
    
    @property
    def federal_vote_count(self):
        federal_total_vote = FederalPoll.objects.all().count()
        count_yes = FederalPoll.objects.filter(choice=CHOICE[0][0]).count()
        if federal_total_vote ==0:
            return f'No user has voted yet!!!'

        result= int((count_yes/federal_total_vote)*100)
        print(f'votes   {count_yes}')
        return f'FG ({result}%)'
    
    @property
    def state_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        state_total_vote = StatePoll.objects.filter(state=voter.state).count()
        count_yes = StatePoll.objects.filter(choice=CHOICE[0][0])
        state_count = count_yes.filter(state=voter.state).count()
        if state_total_vote ==0:
            return f'{self.no_vote} {voter.state} State!!!'
        result = int((state_count/state_total_vote)*100)
        return f'{voter.state} State ({result}%)'
    
    
    @property
    def senatorial_district_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        #sed = Senatorial_district.objects.filter(name=voter.senDis)
        sendist = Senatorial_districtPoll.objects.filter(senatorial_district=voter.senDis).count()
        print(sendist)
        sendist_total_vote = sendist
        print(sendist_total_vote)
        count_yes = Senatorial_districtPoll.objects.filter(choice=CHOICE[0][0])
        sendist_count = count_yes.filter(senatorial_district=voter.senDis).count()
        if sendist_total_vote ==0:
            return f'{self.no_vote} {self.voter.senDis} Senatorial District!!!'
        result = int((sendist_count/sendist_total_vote)*100)
        return f'{self.voter.senDis} Senatorial District ({result}%)'
    
    @property
    def federal_constituency_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        #sed = Senatorial_district.objects.filter(name=voter.senDis)
        federal_constituency_counted = Federal_ConstituentPoll.objects.filter(federal_constituency=voter.fedCon).count()
        #print(sendist)
        fedconst_total_vote = federal_constituency_counted
        #print(fedconst_total_vote)
        count_yes = Federal_ConstituentPoll.objects.filter(choice=CHOICE[0][0])
        fedconst_count = count_yes.filter(federal_constituency=voter.fedCon).count()
        if fedconst_total_vote ==0:
            return f'{self.no_vote} {self.voter.fedCon} Federal Constituency!!!'
        result = int((fedconst_count/fedconst_total_vote)*100)
        return f'{self.voter.fedCon} Federal Constituency ({result}%)'

    @property
    def lga_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        voter_lga=voter.lga
        lga_total_vote = LGAPoll.objects.filter(lga=voter_lga).count()
        count_yes = LGAPoll.objects.filter(choice=CHOICE[0][0])
        lga_count = count_yes.filter(lga=voter_lga).count()
        if lga_total_vote ==0:
            return f'{self.no_vote} {voter_lga} LGA'
        result = int((lga_count/lga_total_vote)*100)
        return f'{voter_lga} LGA ({result}%)'
    

    
    def __str__(self):
        return f'{self.voter} ...checking Performance  Scores ({self.federal_vote_count}) ({self.state_vote_count}) ({self.lga_vote_count}) ({self.senatorial_district_vote_count}) ({self.federal_constituency_vote_count})'
        #>>>>Last Result request date: {self.result_checked_date}'