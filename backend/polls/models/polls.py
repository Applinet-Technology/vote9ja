

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


CHOICE = (('yes','Yes'),('no','No'))

class Poll(models.Model):
    text = models.CharField(max_length=150)
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
        
    # def save(self, *args):
    #     if datetime.date.today() > self.expiry_date.date():
    #         print('Expiry date is invalid!')
    #         #return 'Expiry date is invalid!'
    #     super().save(self, *args, **kwargs, force_insert=False)
    
    def __str__(self):
        return f'{self.manifestoe.manifestoe}'
        
