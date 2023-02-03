

from django.db import models

from django.db.models import Model, CharField, ForeignKey, CASCADE
from .states import State
from .lgas import LGA
from .senatorial_districts import Senatorial_district
from .federal_constituencies import Federal_Constituent

from smart_selects.db_fields import ChainedForeignKey

from politicians.models import Politician, PoliticalParty, State_Rep

from places.niggeo.state_con import NIG_STATE_CONSTITUENCIES

class State_Constituent(Model):
    name = CharField(max_length=50, choices = NIG_STATE_CONSTITUENCIES, default='state constituency')
    state_reps = models.ForeignKey(State_Rep, on_delete=models.CASCADE, related_name = 'state_representative')
    state = ForeignKey(State, on_delete=CASCADE, related_name='con_ward_lga_state')
    
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
    
    def __str__(self):
        return self.get_name_display()
