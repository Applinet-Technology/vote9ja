

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
from politicians.models import Fed_RepParty, Fed_Rep, Fed_House

from .polls import Poll, CHOICE

class Federal_ConstituentPoll(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_fed_rep_manifestoe_details')
    fedCon= ChainedForeignKey(Federal_Constituent,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    rep= ChainedForeignKey(Fed_Rep,
        chained_field="fedCon",
        chained_model_field="fedCon",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    party= ChainedForeignKey(Fed_RepParty,
        chained_field="rep",
        chained_model_field="fedCon",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # rep = models.ForeignKey(Fed_Rep, on_delete=models.CASCADE, related_name='federal_cons_poll_manifestoes')
      
    manifestoe = ChainedForeignKey(Fed_House,
        chained_field="fedCon",
        chained_model_field="fedCon",
        show_all=False, 
        auto_choose=True, 
        sort=True
        )
    text = models.CharField(max_length=150)
    activation_date = models.DateTimeField(auto_now=True)
    expiry_date = models.DateTimeField()
        
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return f'Federal Constituency Representative Manifestoe ({self.manifestoe.manifestoe.manifestoe}) {self.text}' 
    

        
class Federal_ConstituentVote(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='federal_constituent_voter')
    state= ChainedForeignKey(State,
        chained_field="voter",
        chained_model_field="user_state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    # state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_fed_rep_manifestoe_details')
    fedCon= ChainedForeignKey(Federal_Constituent,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    # rep= ChainedForeignKey(Fed_Rep,
    #     chained_field="fedCon",
    #     chained_model_field="fedCon",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True,
    #     )
    # # party= ChainedForeignKey(Fed_RepParty,
    # #     chained_field="rep",
    #     chained_model_field="fedCon",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True,
    #     )

    #poll = models.ForeignKey(Federal_ConstituentPoll, on_delete=models.CASCADE, related_name='federal_constituency_poll')
    poll= ChainedForeignKey(Federal_ConstituentPoll,
        chained_field="fedCon",
        chained_model_field="fedCon",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    rating = models.CharField(max_length=10, choices=CHOICE)
    
    # def save(self, *args, **kwargs):
    #     poll=Federal_ConstituentPoll.objects.get(id=self.poll_id)
    #     poll_is_active=self.poll.poll_is_active
    #     if poll_is_active != True:
    #         return 'Poll no longer active.'
    #     print(poll.expiry_date)
    #     super().save(self, *args, **kwargs)
    
    vote_date = models.DateTimeField(auto_now=True)
    has_voted = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.poll.manifestoe} {self.fedCon}'
   