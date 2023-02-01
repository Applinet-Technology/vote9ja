
'''
from rest_framework import serializers

from  .models import Sector, Manifestoe, Poll, FGPoll, StatePoll, Senatorial_districtPoll, Federal_ConstituentPoll, LGAPoll, State_ConstituentPoll, WardPoll



class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'
        

class ManifestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manifestoe
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    # manifestoe = serializers.SerializerMethodField('get_manifestoe')
    # print(manifestoe)
    # sector_title = getattr('poll__object', 'manifestoe')
    class Meta:
        model = Poll
        fields = ['id','manifestoe','activation_date','expiry_date']

class FGPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = FGPoll
        fields = '__all__'


class StatePollSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatePoll
        fields = '__all__'
        

class Senatorial_districtPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Senatorial_districtPoll
        fields = '__all__'
        

class Federal_ConstituentPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Federal_ConstituentPoll
        fields = '__all__'


class LGAPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = LGAPoll
        fields = '__all__'
        

class State_ConstituentPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = State_ConstituentPoll
        fields = '__all__'
        

class WardPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardPoll
        fields = '__all__'
'''     
