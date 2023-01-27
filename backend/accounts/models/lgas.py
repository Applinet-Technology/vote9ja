
from django.db.models import Model, CharField, ForeignKey, CASCADE
from .states import State
from .senatorial_districts import Senatorial_district
from .federal_constituencies import Federal_Constituent
from smart_selects.db_fields import ChainedForeignKey


class LGA(Model):
    name = CharField(max_length=50, default='lga')
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
    
    
    # lga = ChainedForeignKey(LGA,
    #     chained_field="fedCon",
    #     chained_model_field="federal_constituency",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True
    #     )
    
    # senatorial_district =ForeignKey(Senatorial_district, on_delete=CASCADE, related_name='Senator_district_lga')
    # federal_constituency = ForeignKey(Federal_Constituent, on_delete=CASCADE, related_name='federal_constituency_lga')
    
    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.name
