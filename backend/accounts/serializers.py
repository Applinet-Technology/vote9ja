

from rest_framework.authtoken.models import Token
from rest_framework import serializers

from .models.users import User
from smart_selects.db_fields import ChainedForeignKey
from .models.states import State
from .models.lgas import LGA
from .models.wards import Ward
from .models.locations import PollingLocation
from .models.senatorial_districts import Senatorial_district
from .models.federal_constituencies import Federal_Constituent
from .models.state_constituencies import State_Constituent
from places.niggeo.states import NIG_STATES


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','get_full_name', 'birthdate', 'email', 'phone_number', 'state', 'get_state', 'senDis', 'get_senate', 'fedCon','get_fedcon','lga','get_lga','state_con','get_state_con','ward','location','upload', 'password']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            birthdate=validated_data['birthdate'],
            #gender=validated_data['gender'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            
            state=validated_data['state'],
            
            senDis=validated_data['senDis'],
            
            fedCon=validated_data['fedCon'],
            lga=validated_data['lga'],
            state_con=validated_data['state_con'],
            ward=validated_data['ward'],
            location=validated_data['location'],
            
            )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return User.objects.create(**validated_data)




class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        
# u =UserSerializer
# print(u.__repr__(self))