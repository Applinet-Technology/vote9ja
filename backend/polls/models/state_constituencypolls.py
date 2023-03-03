
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
from accounts.models.state_constituencies import State_Constituent
from politicians.models import State_RepParty, State_Rep, State_House
from .polls import Poll, CHOICE

class State_ConstituentPoll(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_constituency_party_candidate_manifestoe')
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    stateCon= ChainedForeignKey(State_Constituent,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    rep= ChainedForeignKey(State_Rep,
        chained_field="stateCon",
        chained_model_field="stateCon",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    party= ChainedForeignKey(State_RepParty,
        chained_field="rep",
        chained_model_field="rep",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    # rep = models.ForeignKey(State_Rep, on_delete=models.CASCADE, related_name='state_conpoll')
      
    manifestoe = ChainedForeignKey(State_House,
        chained_field="rep",
        chained_model_field="rep",
        show_all=False, 
        auto_choose=True, 
        sort=True
        )
    text = models.CharField(max_length=150)
    activation_date = models.DateTimeField(auto_now=True)
    expiry_date = models.DateTimeField()
        
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'State Constituency Representative Manifestoe ({self.manifestoe.manifestoe.manifestoe}) {self.text}' 
    

   
class State_ConstituentVote(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='state_con_voter', default=1)
    # state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_constituency_party_candidate_manifestoe')
    state= ChainedForeignKey(State,
        chained_field="voter",
        chained_model_field="user_state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    stateCon= ChainedForeignKey(State_Constituent,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # rep= ChainedForeignKey(State_Rep,
    #     chained_field="stateCon",
    #     chained_model_field="stateCon",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True,
    #     )
    # party= ChainedForeignKey(State_RepParty,
    #     chained_field="rep",
    #     chained_model_field="rep",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True,
    #     )
    
    # poll = models.ForeignKey(State_ConstituentPoll, on_delete=models.CASCADE, related_name='state_con_poll')
    poll= ChainedForeignKey(State_ConstituentPoll,
        chained_field="stateCon",
        chained_model_field="stateCon",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    rating = models.CharField(max_length=10, choices=CHOICE)
    vote_date = models.DateTimeField(auto_now=True)
    has_voted = models.BooleanField(default=True)
    
    # def save(self, *args, **kwargs):
    #     poll=State_ConstituentPoll.objects.get(id=self.poll_id)
    #     poll_is_active=self.poll.poll_is_active
    #     if poll_is_active != True:
    #         return 'Poll no longer active.'
    #     print(poll.expiry_date)
    #     super().save(self, *args, **kwargs)
    
    def __str__(self):
        return f'{self.voter} has voted on {self.poll.manifestoe} {self.voter.state_con} Ward performance poll on {self.vote_date}'
