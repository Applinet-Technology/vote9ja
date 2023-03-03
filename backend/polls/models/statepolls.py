

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
from politicians.models import GuberParty, Guber, Gubernatorial

from .polls import CHOICE

class StatePoll(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name = 'state_guber_governor_mandetailks')
    
    # guber= ChainedForeignKey(Guber,
    #     chained_field="state",
    #     chained_model_field="state",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True,
    #     )
    # guber = models.ForeignKey(Guber, on_delete=models.CASCADE)
    party = ChainedForeignKey(GuberParty,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True
        )
    manifestoe = ChainedForeignKey(Gubernatorial,
        chained_field="state",
        chained_model_field="guber",
        show_all=False, 
        auto_choose=True, 
        sort=True
        )
    text = models.CharField(max_length=150)
    activation_date = models.DateTimeField(auto_now=True)
    expiry_date = models.DateTimeField()

    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.manifestoe.manifestoe.manifestoe} ({self.text})'

class StateVote(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='state_voter')
    state= ChainedForeignKey(State,
        chained_field="voter",
        chained_model_field="user_state",
        show_all=False, 
        auto_choose=True,
        sort=True
        )
    # guber= ChainedForeignKey(Guber,
    #     chained_field="state",
    #     chained_model_field="state",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True,
    #     )
    # # guber = models.ForeignKey(Guber, on_delete=models.CASCADE)
    # party = ChainedForeignKey(GuberParty,
    #     chained_field="guber",
    #     chained_model_field="guber",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True
    #     )
    poll = models.ForeignKey(StatePoll, on_delete=models.CASCADE, related_name='state_poll')
    rating = models.CharField(max_length=10, choices=CHOICE)
    vote_date = models.DateTimeField(auto_now=True)
    has_voted = models.BooleanField(default=True)
    
    # def save(self, *args, **kwargs):
    #     poll=StatePoll.objects.get(id=self.poll_id)
    #     poll_is_active=self.poll.poll.poll_is_active
    #     if poll_is_active != True:
    #         return 'Poll no longer active.'
    #     print(poll.poll.expiry_date)
    #     super().save(self, *args, **kwargs)
    
    def __str__(self):
        return f'{self.poll.manifestoe.manifestoe.manifestoe} {self.state} State performance poll on {self.vote_date}'
