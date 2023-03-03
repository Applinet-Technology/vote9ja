


from django.db import models
from .senatorial_districts import Senatorial_district
from .states import State
from smart_selects.db_fields import ChainedForeignKey

# from politicians.models import Politician, PoliticalParty, Fed_Rep

from places.niggeo.fed_con import NIG_FEDERAL_CONSTITUENCIES

class Federal_Constituent(models.Model):
    name = models.CharField(max_length=50, choices=NIG_FEDERAL_CONSTITUENCIES, unique=True)
    # representative = models.ForeignKey(Fed_Rep, on_delete=models.CASCADE, related_name = 'representative')
    
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='Federal_Constituent_state')
    
    senDis= ChainedForeignKey(Senatorial_district,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
        
    @property
    def get_fed_con_name(self):
        return self.get_name_display()

    
    def __str__(self):
        return self.get_name_display()