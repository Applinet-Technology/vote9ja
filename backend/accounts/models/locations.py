

from django.db import models

from smart_selects.db_fields import ChainedForeignKey


from .federal import Federal
from .states import State
from .senatorial_districts import Senatorial_district
from .federal_constituencies import Federal_Constituent
from .lgas import LGA
from .wards import Ward


class PollingLocation(models.Model):
    name = models.CharField(max_length=100, default='location')
    
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='location_ward_lga_state', default=1)
    
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
    
    def __str__(self):
        return self.name



