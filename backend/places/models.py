

from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from .niggeo.lgas import NIG_LGAS
from .niggeo.states import NIG_STATES

class PState(models.Model):
    name = models.CharField(max_length=50, choices = NIG_STATES, unique=True)
    #guber = models.ForeignKey(Guber, on_delete=models.CASCADE, related_name = 'governorship')
    
    def __str__(self):
        return self.get_name_display()

class PLGA(models.Model):
    state = models.ForeignKey(PState, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50, choices=NIG_LGAS, unique=True)
    #guber = models.ForeignKey(Guber, on_delete=models.CASCADE, related_name = 'governorship')
    
    def __str__(self):
        return self.get_name_display()



# senDis= ChainedForeignKey(Senatorial_district,
#         chained_field="state",
#         chained_model_field="state",
#         show_all=False, 
#         auto_choose=True, 
#         sort=True,
#         )
