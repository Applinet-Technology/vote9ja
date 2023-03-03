


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
from politicians.models import CouncilorshipParty, Councilorship, WardCouncilorship

from .polls import Poll, CHOICE

class WardPoll(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_councilor_councilorship')
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    ward= ChainedForeignKey(Ward,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    councilorship= ChainedForeignKey(Councilorship,
        chained_field="ward",
        chained_model_field="ward",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    party= ChainedForeignKey(CouncilorshipParty,
        chained_field="councilorship",
        chained_model_field="councilorship",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # councilorship= models.ForeignKey(Councilorship, on_delete=models.CASCADE, related_name='ward_counpoll')
      
    manifestoe = ChainedForeignKey(WardCouncilorship,
        chained_field="councilorship",
        chained_model_field="councilorship",
        show_all=False, 
        auto_choose=True, 
        sort=True
        )
    text = models.CharField(max_length=150)
    activation_date = models.DateTimeField(auto_now=True)
    expiry_date = models.DateTimeField()
        
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'Ward Councilor Manifestoe ({self.manifestoe.manifestoe.manifestoe}) {self.text}' 
    
   
class WardVote(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='ward_voter')
    state= ChainedForeignKey(State,
        chained_field="voter",
        chained_model_field="user_state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_councilor_councilorship_vote')
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    ward= ChainedForeignKey(Ward,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # councilorship= ChainedForeignKey(Councilorship,
    #     chained_field="ward",
    #     chained_model_field="ward",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True,
    #     )
    # party= ChainedForeignKey(CouncilorshipParty,
    #     chained_field="councilorship",
    #     chained_model_field="councilorship",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True,
    #     )
    poll= ChainedForeignKey(WardPoll,
        chained_field="ward",
        chained_model_field="ward",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    rating = models.CharField(max_length=10, choices=CHOICE)
    vote_date = models.DateTimeField(auto_now=True)
    has_voted = models.BooleanField(default=True)
    
    # def save(self, *args, **kwargs):
    #     poll=WardPoll.objects.get(id=self.poll_id)
    #     poll_is_active=self.poll.poll_is_active
    #     if poll_is_active != True:
    #         return 'Poll no longer active.'
    #     print(poll.expiry_date)
    #     super().save(self, *args, **kwargs)
    
    def __str__(self):
        return f'{self.voter} has voted on {self.poll.manifestoe} {self.voter.ward} Ward performance poll on {self.vote_date}'
