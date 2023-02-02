
from django.db import models
from .states import State
from politicians.models import Politician, PoliticalParty, Senate
from places.niggeo.sen_dist import NIG_SENATORIAL_DISTRICTS
#from smart_selects.db_fields import ChainedForeignKey


class Senatorial_district(models.Model):
    name = models.CharField(max_length=50, choices =NIG_SENATORIAL_DISTRICTS,unique=True)
    senate = models.ForeignKey(Senate, on_delete=models.CASCADE, related_name = 'senate')
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='sendistrict_state')

    
    def __str__(self):
        return self.get_name_display()