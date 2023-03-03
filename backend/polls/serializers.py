

from rest_framework import serializers

from  .models import Poll, FGPoll, StatePoll, Senatorial_districtPoll, Federal_ConstituentPoll, LGAPoll, State_ConstituentPoll, WardPoll, FGVote, StateVote, Senatorial_districtVote, Federal_ConstituentVote, LGAVote, State_ConstituentVote, WardVote, Result



class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

class FGPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = FGPoll
        fields = '__all__'

class FGVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FGVote
        fields = '__all__'
        
        #['voter','poll','rating']


class StatePollSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatePoll
        fields = '__all__'
        
class StateVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateVote
        fields = '__all__'
        
        #['voter','state','poll','rating']



class Senatorial_districtPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Senatorial_districtPoll
        fields = '__all__'
        
class Senatorial_districtVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Senatorial_districtVote
        fields = '__all__'
    
    #['voter','state','senDis','poll','rating']



class Federal_ConstituentPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Federal_ConstituentPoll
        fields = '__all__'

class Federal_ConstituentVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Federal_ConstituentVote
        fields = '__all__'
        #['voter','state','fedCon','poll','rating']






class LGAPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = LGAPoll
        fields = '__all__'
        
class LGAVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LGAVote
        fields = '__all__'
        
        #['voter','state','lga','poll','rating']



class State_ConstituentPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = State_ConstituentPoll
        fields = '__all__'
        
class State_ConstituentVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = State_ConstituentVote
        fields = '__all__'
        #['voter','state','lga','stateCon','poll','rating']


        

class WardPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardPoll
        fields = '__all__'

class WardVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = WardVote
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=Result
        fields=[]
        
