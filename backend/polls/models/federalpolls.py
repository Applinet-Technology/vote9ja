

import datetime
from django.utils import timezone
from django.db import models
from accounts.models.users import User
from smart_selects.db_fields import ChainedForeignKey

from accounts.models.states import State
from accounts.models.senatorial_districts import Senatorial_district
from accounts.models.federal_constituencies import Federal_Constituent
from accounts.models.lgas import LGA
from accounts.models.wards import Ward

from politicians.models import Presidency

from politicians.models import PresidencyParty, Presidency, Presidential
from . import Poll, CHOICE


class FGPoll(models.Model):
    presidency= models.ForeignKey(Presidency, on_delete=models.CASCADE, related_name = 'federal_presidency')
    
    party = ChainedForeignKey(PresidencyParty,
        chained_field="presidency",
        chained_model_field="presidency",
        show_all=False, 
        auto_choose=True, 
        sort=True
        )
        
    manifestoe = ChainedForeignKey(Presidential,
        chained_field="presidency",
        chained_model_field="presidency",
        show_all=False, 
        auto_choose=True, 
        sort=True
        )
    text = models.CharField(max_length=150)
    activation_date = models.DateTimeField(auto_now=True)
    expiry_date = models.DateTimeField()
    
    is_active = models.BooleanField(default=True)
    
    def was_activated_recently(self):
        return self.activation_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return f' {self.text} on {self.manifestoe.manifestoe.manifestoe}' 
    
class FGVote(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='federal_voter')
    presidency= models.ForeignKey(Presidency, on_delete=models.CASCADE, related_name = 'federal_presidency_fgvote', default=1)
    
    # party = ChainedForeignKey(PresidencyParty,
    #     chained_field="presidency",
    #     chained_model_field="presidency",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True
    #     )
        
    # manifestoe = ChainedForeignKey(Presidential,
    #     chained_field="presidency",
    #     chained_model_field="presidency",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True
    #     )
    
    poll = ChainedForeignKey(FGPoll,
        chained_field="presidency",
        chained_model_field="presidency",
        show_all=False, 
        auto_choose=True, 
        sort=True
        )
    # poll = models.ForeignKey(FGPoll, on_delete=models.CASCADE, related_name='federal_poll')
    rating = models.CharField(max_length=10, choices=CHOICE)
    vote_date = models.DateTimeField(auto_now_add=True)
    has_voted = models.BooleanField(default=True)
    @property
    def poll_is_active(self):
        expiry =self.poll.expiry_date.date()
        current=datetime.date.today()
        if current<expiry:
            return True
        return False
    
    
    # def save(self, *args, **kwargs):
    #     poll_is_active=self.poll_is_active
    #     if poll_is_active != True:                print('Poll no longer active.')
    #     print(self.expiry_date)
    #     super().save(self, *args, **kwargs)
    
    
    
    def __str__(self):
        return f'{self.poll.manifestoe.manifestoe.manifestoe} performance poll on {self.vote_date}'
