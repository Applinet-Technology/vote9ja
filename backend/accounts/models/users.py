from django.db.models import Model
from django.contrib.auth.models import User
from django.db.models import Model, CharField, DateField, ForeignKey,IntegerField, CASCADE
from smart_selects.db_fields import ChainedForeignKey
from .states import State

from .lgas import LGA

from .wards import Ward
from .senatorial_districts import Senatorial_district
from .federal_constituencies import Federal_Constituent


class User(User):
    birthdate = DateField()
    gender = CharField(max_length=7, choices=(('male','Male'), ('female', 'Female')))
    phone_number=IntegerField(default='+234')
    state = ForeignKey(State, on_delete=CASCADE, related_name='user_state')
    #lga = GroupedForeignKey(LGA, "state")
    #ward = GroupedForeignKey(Ward, "lga")
    senDis= ChainedForeignKey(Senatorial_district,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    fedCon= ChainedForeignKey(Federal_Constituent,
        chained_field="senDis",
        chained_model_field="senDis",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    
    lga = ChainedForeignKey(LGA,
        chained_field="fedCon",
        chained_model_field="fedCon",
        show_all=False, 
        auto_choose=True, 
        sort=True
        )
        
    ward = ChainedForeignKey(Ward,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True
        )
        
    
        
    # @property
    # def senatorial_district(self):
    #     lga = LGA.objects.get(name =self.lga)
    #     sd = lga.senatorial_district
    #     return f'{sd}'
    
    # @property
    # def federal_constituency(self):
    #     lga = LGA.objects.get(name =self.lga)
    #     fc = lga.federal_constituency
    #     return f'{fc} Federal Constituency'
    
        
        #sd= Senatorial_district.objects.get(=self.voter)
        
        # voter_state=voter.state
        # state_total_vote = StatePoll.objects.filter(state=voter_state).count()
    
    
    # def save(self, *args, **kwargs):
    #     import datetime
    #     if self.birthdate > datetime.date(2005, 1, 1):
    #         return "You're not 18r"
    #     else:
    #         super().save(*args, **kwargs)
    #     # Call the "real" save() method.
        

    
    
    def __str__(self):
        return f'{self.username}'
