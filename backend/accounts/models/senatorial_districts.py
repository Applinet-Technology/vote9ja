
from django.db import models
from .states import State
from smart_selects.db_fields import ChainedForeignKey


class Senatorial_district(models.Model):
    name = models.CharField(max_length=50, unique=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='sendistrict_state')
    
    def __str__(self):
        return self.name