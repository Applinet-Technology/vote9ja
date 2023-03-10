
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

from .polls import Poll, CHOICE

from politicians.models import Senate, Senatorial


class Senatorial_districtPoll(models.Model):
    senate = models.ForeignKey(Senate, on_delete=models.CASCADE)
      
    manifestoe = ChainedForeignKey(Senatorial,
        chained_field="senate",
        chained_model_field="senate",
        show_all=False, 
        auto_choose=True, 
        sort=True
        )
    text = models.CharField(max_length=150)
    activation_date = models.DateTimeField(auto_now=True)
    expiry_date = models.DateTimeField()
        
    is_active = models.BooleanField(default=True)

class Senatorial_districtVote(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='senatorial_district_voter')
    
    senatorial_district= ChainedForeignKey(Senatorial_district,
        chained_field="voter",
        chained_model_field="user",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    poll = models.ForeignKey(Senatorial_districtPoll, on_delete=models.CASCADE, related_name='senatorial_district_poll', default=1)
    choice = models.CharField(max_length=10, choices=CHOICE)
    vote_date = models.DateTimeField(auto_now=True)
    has_voted = models.BooleanField(default=True)
    
    # def save(self, *args, **kwargs):
    #     poll=Senatorial_districtPoll.objects.get(id=self.poll_id)
    #     poll_is_active=self.poll.poll_is_active
    #     if poll_is_active != True:
    #         return 'Poll no longer active.'
    #     print(poll.expiry_date)
    #     super().save(self, *args, **kwargs)
    
    def __str__(self):
        return f'{self.poll.manifestoe.manifestoe.manifestoe_title} {self.senatorial_district}'
        