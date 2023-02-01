
from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework.validators import UniqueValidator

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models.users import User
from smart_selects.db_fields import ChainedForeignKey
from .models.states import State

from .models.lgas import LGA

from .models.wards import Ward
from .models.locations import PollingLocation
from .models.senatorial_districts import Senatorial_district
from .models.federal_constituencies import Federal_Constituent
from .models.state_constituencies import State_Constituent

from rest_framework.authtoken.models import Token
from rest_framework import serializers
from places.niggeo.states import NIG_STATES

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','get_full_name', 'birthdate', 'gender', 'email', 'phone_number', 'state', 'get_state', 'senDis', 'get_senate', 'fedCon','get_fedcon','lga','get_lga','state_con','get_state_con','ward','location', 'password']

#'get_fedcon','get_lga', 'get_state_con'

# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[UniqueValidator(User.objects.all()),])
#     first_name = serializers.CharField(allow_blank=True, max_length=150, required=False)
#     last_name = serializers.CharField(allow_blank=True, max_length=150, required=False)
#     get_full_name = serializers.ReadOnlyField()
#     birthdate = serializers.DateField()
#     gender = serializers.ChoiceField(choices=(('male', 'Male'), ('female', 'Female')))
#     email = serializers.EmailField(allow_blank=True, label='Email address', max_length=254, required=False)
#     phone_number = serializers.IntegerField()
#     state = serializers.PrimaryKeyRelatedField(queryset=State.objects.all())
    
    #state = serializers.ChoiceField(choices=[(x,y) for x, y in NIG_STATES])
    
    # senDis = serializers.PrimaryKeyRelatedField(label='SenDis', queryset=Senatorial_district.objects.all())
    # fedCon = serializers.PrimaryKeyRelatedField(label='FedCon', queryset=Federal_Constituent.objects.all())
    # lga = serializers.PrimaryKeyRelatedField(queryset=LGA.objects.all())
    # state_con = serializers.PrimaryKeyRelatedField(queryset=State_Constituent.objects.all())
    # ward = serializers.PrimaryKeyRelatedField(queryset=Ward.objects.all())
    # location = serializers.PrimaryKeyRelatedField(queryset=PollingLocation.objects.all()) 
    # password = serializers.CharField(max_length=128)
    
    
    def create(self, validated_data):
        #user = User(
            # username=validated_data['username'],
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name'],
            # birthdate=validated_data['birthdate'],
            # gender=validated_data['gender'],
            # email=validated_data['email'],
            # phone_number=validated_data['phone_number'],
            
            # state=validated_data['state'],
            
            # senDis=validated_data['senDis'],
            
            # fedCon=validated_data['fedCon'],
            # lga=validated_data['lga'],
            # state_con=validated_data['state_con'],
            # ward=validated_data['ward'],
            # location=validated_data['location'],
            
            # )
        #user.set_password(validated_data['password'])
        #user.save()
        #Token.objects.create(user=user)
        return User.objects.create(**validated_data)
# seriy=UserSerializer()
# print(repr(seriy))
        

# class BlogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blog
#         fields = ['category', 'title', 'body', 'date', 'blogger', 'username']
#         order_by = ['date',]'''


# sta=State.objects.all()
# u=0
# y = [x for x in sta]
# print(y[u])