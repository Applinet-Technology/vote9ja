
from django.db.models import Model, CharField, ForeignKey, CASCADE, OneToOneField
from .states import State
from .senatorial_districts import Senatorial_district
from .federal_constituencies import Federal_Constituent
from smart_selects.db_fields import ChainedForeignKey

from politicians.models import Politician, PoliticalParty, Chairmanship
from places.models import NIG_LGAS

class LGA(Model):
    name = CharField(max_length=50, choices = NIG_LGAS, default='lga')
    chairmanship = ForeignKey(Chairmanship, on_delete=CASCADE, related_name = 'chairmanship')
    state = ForeignKey(State, on_delete=CASCADE, related_name='lga_state')
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
    
    def __str__(self):
        return self.get_name_display()
