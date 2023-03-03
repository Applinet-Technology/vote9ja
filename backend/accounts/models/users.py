import sys
from geography import Countries
import uuid
from django.db.models import Model
from django.contrib.auth.models import User
from django.db.models import Model, CharField, DateField, ForeignKey,IntegerField, CASCADE, FileField,UUIDField
from smart_selects.db_fields import ChainedForeignKey
from .states import State

from .lgas import LGA

from .wards import Ward
from .locations import PollingLocation
from .senatorial_districts import Senatorial_district
from .federal_constituencies import Federal_Constituent
from .state_constituencies import State_Constituent

import datetime



# def images_path():
#     return os.path.join(settings.LOCAL_FILE_DIR, 'images')

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format('vote9ja/users/', filename)

# class MyModel(models.Model):
#     upload = models.FileField(upload_to=user_directory_path)

class User(User):
    #reg_id= UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    birthdate = DateField(default='1960/10/01')
    #gender = CharField(max_length=7, choices=(('male','Male'), ('female', 'Female')))
    phone_number=IntegerField()
    state = ForeignKey(State, on_delete=CASCADE, related_name='user_state')
    #lga = GroupedForeignKey(LGA, "state")
    #ward = GroupedForeignKey(Ward, "lga")
    
    senDis= ChainedForeignKey(Senatorial_district,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True
        )
        
    fedCon= ChainedForeignKey(Federal_Constituent,
        chained_field="senDis",
        chained_model_field="senDis",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        null=True,
        blank=True
        )
    
    
    lga = ChainedForeignKey(LGA,
        chained_field="fedCon",
        chained_model_field="fedCon",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        null=True,
        blank=True
        )
        
    state_con = ChainedForeignKey(State_Constituent,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        null=True,
        blank=True
        )
    
    
        
    ward = ChainedForeignKey(Ward,
        chained_field="state_con",
        chained_model_field="state_con",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        null=True,
        blank=True
        )
    
    location = ChainedForeignKey(PollingLocation,
        chained_field="ward",
        chained_model_field="ward",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        null=True,
        blank=True
        )
    upload = FileField(upload_to=user_directory_path)
    
    @property
    def get_state(self):
        return self.state.get_name_display()
    
    @property
    def get_senate(self):
        return self.senDis.get_name_display()
    
    @property
    def get_fedcon(self):
        return self.fedCon.get_name_display()
    
    @property
    def get_lga(self):
        return self.lga.get_name_display()
        
    @property
    def get_state_con(self):
        return self.state_con.get_name_display()


    
    def __str__(self):
        print(f'{self.username}')
        return f'{self.username}'
    
    def __hash__(self):
        print(f'Representation>>>>{hash(self.username)}')


class Full:
    pass


# user=Full

# user.__setattr__(name, 'sam')

y,z =519, 'theses'
print(f'result...{z.__len__()} & {y}')

# af=Countries.getPopulationRanking('nigeria')

# print(user)
print(sys.hash_info.width)
        

# class A:
# ,   pass
# descr = custom_descriptor()
# A.attr = descr
# descr.__set_name__(A, 'attr')