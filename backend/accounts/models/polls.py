
from django.db import models
from .users import User
from smart_selects.db_fields import ChainedForeignKey
from .federal import Federal
from .states import State
from .senatorial_districts import Senatorial_district
from .federal_constituencies import Federal_Constituent
from .lgas import LGA


class Sector(models.Model):
    name = models.CharField(max_length=50, default='Sector', unique=True)
    
    def __str__(self):
        return self.name

class Manifestoe(models.Model):
    sector = models.OneToOneField(Sector, on_delete=models.CASCADE, related_name='manifestoe_sector')
    manifestoe = models.TextField()
    def __str__(self):
        return f'{self.sector}: {self.manifestoe}'
        
class FederalPoll(models.Model):
    #voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='federal_voter')
    manifestoe = models.ForeignKey(Manifestoe, on_delete=models.CASCADE, related_name='manifestoe_federal_poll')
    choice = models.CharField(max_length=3, choices=(('yes','Yes'),('no','No')))
    vote_date = models.DateTimeField(auto_now=True)
    has_voted = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.manifestoe.sector} performance poll on {self.vote_date}'

class StatePoll(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='state_voter')
    #state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_poll_vote')
    state= ChainedForeignKey(State,
        chained_field="voter",
        chained_model_field="user_state",
        show_all=False, 
        auto_choose=True,
        sort=True
        )
    
    #state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_poll')
    manifestoe = models.ForeignKey(Manifestoe, on_delete=models.CASCADE, related_name='manifestoe_state_poll')
    choice = models.CharField(max_length=3, choices=(('yes','Yes'),('no','No')))
    vote_date = models.DateTimeField(auto_now=True)
    has_voted = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.manifestoe.sector} {self.state} State performance poll on {self.vote_date}'

class Senatorial_districtPoll(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='senatorial_district_voter')
    
    senatorial_district= ChainedForeignKey(Senatorial_district,
        chained_field="voter",
        chained_model_field="state_id",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    # senatorial_district= models.ForeignKey(Senatorial_district, on_delete=models.CASCADE, related_name='Senatorial_district_poll')
    # # lga= ChainedForeignKey(LGA,
    #     chained_field="senatorial_district",
    #     chained_model_field="senatorial_district",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True,
    #     )
    
    manifestoe = models.ForeignKey(Manifestoe, on_delete=models.CASCADE, related_name='manifestoe_senatorial_district_poll')
    choice = models.CharField(max_length=3, choices=(('yes','Yes'),('no','No')))
    vote_date = models.DateTimeField(auto_now=True)
    has_voted = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.senatorial_district}'
        

class Federal_ConstituentPoll(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='Federal_Constituent_voter')
    #federal_constituency= models.ForeignKey(Federal_Constituent, on_delete=models.CASCADE, related_name='Federal_Constituent_poll')
    manifestoe = models.ForeignKey(Manifestoe, on_delete=models.CASCADE, related_name='manifestoe_federal_const_poll')
    choice = models.CharField(max_length=3, choices=(('yes','Yes'),('no','No')))
    vote_date = models.DateTimeField(auto_now=True)
    has_voted = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.voter} has voted on {self.manifestoe.sector} {self.voter.federal_constituency} federal constituency performance poll on {self.vote_date}'
        

    

class LGAPoll(models.Model):
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='lga_voter')
    lga= ChainedForeignKey(LGA,
        chained_field="voter",
        chained_model_field="user",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    #lga = models.ForeignKey(LGA, on_delete=models.CASCADE, related_name='lga_poll')
    manifestoe = models.ForeignKey(Manifestoe, on_delete=models.CASCADE, related_name='manifestoe_lga_poll')
    choice = models.CharField(max_length=3, choices=(('yes','Yes'),('no','No')))
    vote_date = models.DateTimeField(auto_now=True)
    has_voted = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.voter} has voted on {self.manifestoe.sector} {self.voter.lga} LGA performance poll on {self.vote_date}'
        



class Result(models.Model):
    #state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='voter_result')
    voter= models.ForeignKey(User, on_delete=models.CASCADE, related_name='voter_user_result', blank=True, null=True)
    result_checked_date = models.DateTimeField(auto_now=True)
    no_vote = 'No vote has been made by users yet!'
    
    @property
    def federal_vote_count(self):
        federal_total_vote = FederalPoll.objects.all().count()
        count_yes = FederalPoll.objects.filter(choice='yes').count()
        if federal_total_vote ==0:
            return f'FG ({self.no_vote})'

        result= int((count_yes/federal_total_vote)*100)
        return f'FG ({result}%)'
    
    @property
    def state_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        
        #voter_state=self.voter.state
        state_total_vote = StatePoll.objects.filter(state=voter.state).count()
        count_yes = StatePoll.objects.filter(choice='yes')
        state_count = count_yes.filter(state=voter.state).count()
        if state_total_vote ==0:
            return f'{voter.state} State ({self.no_vote})'
        result = int((state_count/state_total_vote)*100)
        return f'{voter.state} State ({result}%)'
    
    
    @property
    def senatorial_district_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        #sed = Senatorial_district.objects.filter(name=voter.senDis)
        sendist = Senatorial_districtPoll.objects.filter(senatorial_district=voter.senDis).count()
        print(sendist)
        sendist_total_vote = sendist
        print(sendist_total_vote)
        count_yes = Senatorial_districtPoll.objects.filter(choice='yes')
        sendist_count = count_yes.filter(senatorial_district=voter.senDis).count()
        if sendist_total_vote ==0:
            return f'{sendist} Senatorial District ({self.no_vote})'
        result = int((sendist_count/sendist_total_vote)*100)
        return f'{voter.senDis} Senatorial District({result}%)'
    
    
    # @property
    # def federal_constituency_vote_count(self):
    #     voter= User.objects.get(username=self.voter)
    #     voter_fedconst=voter.lga.federal_constituency
    #     fedconst = Federal_ConstituentPoll.objects.filter(federal_constituency=voter_fedconst)
    #     fedconst_total_vote = fedconst.count()
    #     count_yes = Federal_ConstituentPoll.objects.filter(choice='yes')
    #     fedconst_count = count_yes.filter(federal_constituency=voter_fedconst).count()
    #     if fedconst_total_vote ==0:
    #         return f'{voter_fedconst} Federal Constituency ({self.no_vote})'
    #     result = int((fedconst_count/fedconst_total_vote)*100)
    #     return f'{voter_fedconst} Federal Constituency ({result}%)'
    
    
    
    @property
    def lga_vote_count(self):
        voter= User.objects.get(id=self.voter_id)
        voter_lga=voter.lga
        lga_total_vote = LGAPoll.objects.filter(lga=voter_lga).count()
        count_yes = LGAPoll.objects.filter(choice='yes')
        lga_count = count_yes.filter(lga=voter_lga).count()
        if lga_total_vote ==0:
            return f'{voter_lga} LGA ({self.no_vote})'
        result = int((lga_count/lga_total_vote)*100)
        return f'{voter_lga} LGA ({result}%)'
    

    
    def __str__(self):
        return f'...checking Performance  Scores ... {self.federal_vote_count} >>>>>>>>> {self.state_vote_count} >>>>>>>>>>> {self.lga_vote_count}>>>>>>>>>>> {self.senatorial_district_vote_count}' '''>>>>>>>>>>> {self.federal_constituency_vote_count}'''