


from django.db import models
from .senatorial_districts import Senatorial_district
from .states import State
from smart_selects.db_fields import ChainedForeignKey


class Federal_Constituent(models.Model):
    name = models.CharField(max_length=50, unique=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='Federal_Constituent_state')
    senDis= ChainedForeignKey(Senatorial_district,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )

    
    def __str__(self):
        return self.name