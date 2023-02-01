

from .federal import Federal
from django.db import models
from politicians.models import Guber
from places.niggeo.states import NIG_STATES

class State(Federal):
    name = models.CharField(max_length=10, choices=NIG_STATES, default='state', unique=True)
    guber = models.ForeignKey(Guber, on_delete=models.CASCADE, related_name = 'governorship')
    
    def __str__(self):
        return self.get_name_display()
