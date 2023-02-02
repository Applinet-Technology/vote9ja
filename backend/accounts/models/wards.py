

from django.db import models
from django.db.models import Model, CharField, ForeignKey, CASCADE
from .states import State
from .lgas import LGA
from .senatorial_districts import Senatorial_district
from .federal_constituencies import Federal_Constituent
from .state_constituencies import State_Constituent

from smart_selects.db_fields import ChainedForeignKey

from politicians.models import Politician, PoliticalParty, Councilorship


class Ward(Model):
    name = CharField(max_length=20, default='ward')
    councilorship = models.ForeignKey(Councilorship, on_delete=models.CASCADE, related_name = 'councilorship')
    state = ForeignKey(State, on_delete=CASCADE, related_name='ward_lga_state')
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
    state_con = ChainedForeignKey(State_Constituent,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True
        )
    
    def __str__(self):
        return self.name
