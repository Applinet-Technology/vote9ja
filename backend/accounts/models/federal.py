

from django.db import models




class Federal(models.Model):
    country = models.CharField(max_length=7, default='Nigeria')
    
    def __str__(self):
        return f'Federal Republic of {country}'