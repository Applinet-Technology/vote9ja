

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
from politicians.models import ChairmanshipParty, Chairmanship, LGAChairmanship

from .polls import Poll, CHOICE

class LGAPoll(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_lgapollchairmanship_candidate')
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    chairmanship= ChainedForeignKey(Chairmanship,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
            
    party= ChainedForeignKey(ChairmanshipParty,
        chained_field="chairmanship",
        chained_model_field="chairmanship",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # chairmanship = models.ForeignKey(Chairmanship, on_delete=models.CASCADE)
      
    manifestoe = ChainedForeignKey(LGAChairmanship,
        chained_field="chairmanship",
        chained_model_field="chairmanship",
        show_all=False, 
        auto_choose=True, 
        sort=True
        )
    text = models.CharField(max_length=150)
    activation_date = models.DateTimeField(auto_now=True)
    expiry_date = models.DateTimeField()

    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.manifestoe.manifestoe.manifestoe.manifestoe} ({self.text})'

class LGAVote(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='lga_voter')
    state= ChainedForeignKey(State,
        chained_field="voter",
        chained_model_field="user_state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
        
    # state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_lgapollchairmanship_candidate')
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="fedCon",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # chairmanship= ChainedForeignKey(Chairmanship,
    #     chained_field="lga",
    #     chained_model_field="lga",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True,
    #     )
            
    # party= ChainedForeignKey(ChairmanshipParty,
    #     chained_field="chairmanship",
    #     chained_model_field="chairmanship",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True,
    #     )
    poll= ChainedForeignKey(LGAPoll,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # poll = models.ForeignKey(LGAPoll, on_delete=models.CASCADE, related_name='lga_poll', default=1)
    rating = models.CharField(max_length=10, choices=CHOICE)
    vote_date = models.DateTimeField(auto_now=True)
    has_voted = models.BooleanField(default=True)
    
    # def save(self, *args, **kwargs):
    #     poll=LGAPoll.objects.get(id=self.poll_id)
    #     poll_is_active=self.poll.poll_is_active
    #     if poll_is_active != True:
    #         return 'Poll no longer active.'
    #     print(poll.expiry_date)
    #     super().save(self, *args, **kwargs)
    
    def __str__(self):
        return f'{self.voter} has voted on {self.poll.manifestoe} {self.voter.lga} LGA performance poll on {self.vote_date}'

   