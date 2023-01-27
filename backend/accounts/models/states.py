

from .federal import Federal
from django.db import models

class State(Federal):
    #federal=models.ForeignKey(Federal, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, default='state', unique=True)
    
    def __str__(self):
        return self.name
