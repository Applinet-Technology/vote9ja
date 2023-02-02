from django.db import models
from political_parties.parties.manifestoes import MANIFESTOES, MANIFESTOE_DETAILS
from political_parties.parties.inec_parties import REGISTERED_PARTIES



class PoliticalParty(models.Model):
    name = models.CharField(max_length=100, choices=REGISTERED_PARTIES)
        
    def __str__(self):
        return f'{self.get_name_display()}'
        #{self.get_manifestoe_display()}'
        
class PartyManifestoe(models.Model):
    manifestoe=models.CharField(max_length=250, choices=MANIFESTOES)
    source = models.URLField(max_length=200)
    def __str__(self):
        return f'{self.get_manifestoe_display()}'
        

class PartyManifestoeDetail(models.Model):
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name='political_party_manifesto_detail')
    manifestoe = models.ForeignKey(PartyManifestoe, on_delete=models.CASCADE,related_name='political_party_manifesto')
    detail=models.CharField(max_length=250, choices=MANIFESTOE_DETAILS)
    def __str__(self):
        return f'{self.get_detail_display()}'
    

class Politician(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100)
    @property
    def presidency(self):
        return f'{self.first_name} {self.surname}'
    @property
    def guber(self):
        return f'{self.first_name} {self.surname}'
    @property
    def senate(self):
        return f'{self.first_name} {self.surname}'
    @property
    def fed_reps(self):
        return f'{self.first_name} {self.surname}'
    @property
    def chairmanship(self):
        return f'{self.first_name} {self.surname}'
    @property
    def state_reps(self):
        return f'{self.first_name} {self.surname}'
    @property
    def councilorship(self):
        return f'{self.first_name} {self.surname}'
    
    def __str__(self):
        return f'{self.first_name} {self.surname}'
 

class CandidateManifestoe(models.Model):
    manifestoe = models.CharField(max_length=200, unique=True)
    source = models.URLField(max_length=200)
    
    def __str__(self):
        return f'{self.manifestoe}'

class CandidateManifestoeDetail(models.Model):
    manifestoe = models.ForeignKey(CandidateManifestoe, on_delete=models.CASCADE, related_name='candidate_manifestoe_politician')
    detail = models.TextField(unique=True)
    def __str__(self):
        return f'{self.detail}'

class Presidency(models.Model):
    president = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'presidency_president')
    vice_president = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'presidency_vice_president')
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name = 'presidency_party')
    
    def __str__(self):
        return f'{self.president.presidency} (President) {self.vice_president.presidency} ({self.party.name})'
        


class Presidential(models.Model):
    presidency = models.OneToOneField(Presidency, on_delete=models.CASCADE)
    manifestoe = models.ForeignKey(CandidateManifestoeDetail,on_delete=models.CASCADE, related_name='presidential_manifestoe_poll')
    
    def __str__(self):
        return f'{self.manifestoe.manifestoe.manifestoe}'

    
class Guber(models.Model):
    governor = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'guber_governor')
    deputy_governor = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'guber_deputy_governor')
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name = 'guber_party')
    
    def __str__(self):
        return f'{self.governor.guber} (Governor) {self.deputy_governor.guber} ({self.ruling_party.name})'
        
class Gubernatorial(models.Model):
    guber = models.ForeignKey(Guber, on_delete=models.CASCADE)
    manifestoe = models.ForeignKey(CandidateManifestoeDetail,on_delete=models.CASCADE, related_name='guber_manifestoe_poll')
    
    def __str__(self):
        return f'{self.guber}'


class Senate(models.Model):
    senator = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'senate_senator')
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name = 'senator_pol_party')
    
    def __str__(self):
        return f'{self.senator.senate} (Senator) ({self.party.name})'
        
class Senatorial(models.Model):
    senate = models.ForeignKey(Senate, on_delete=models.CASCADE)
    manifestoe = models.ForeignKey(CandidateManifestoeDetail,on_delete=models.CASCADE, related_name='senate_manifestoe_poll')
    
    def __str__(self):
        return f'{self.senate}'

    
        
class Fed_Rep(models.Model):
    rep = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'fed_reps_rep')
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name = 'fed_reps_pol_party')
    
    def __str__(self):
        return f'{self.rep.fed_reps} (Federal Representative) ({self.party.name})'

class Fed_House(models.Model):
    rep = models.ForeignKey(Fed_Rep, on_delete=models.CASCADE)
    manifestoe = models.ForeignKey(CandidateManifestoeDetail,on_delete=models.CASCADE, related_name='fedrep_manifestoe_poll')
    
    def __str__(self):
        return f'{self.rep}'
        

class Chairmanship(models.Model):
    chairman = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'chairmanship_chairman')
    vice_chairman= models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'chairmanship_vice_chairman')
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name = 'chairmanship_party')
    
    def __str__(self):
        return f'{self.chairman.chairmanship} (Chairman) {self.vice_chairman.chairmanship} ({self.party.name})'
        
        
class LGAChairmanship(models.Model):
    chairmanship = models.ForeignKey(Chairmanship, on_delete=models.CASCADE)
    manifestoe = models.ForeignKey(CandidateManifestoeDetail,on_delete=models.CASCADE, related_name='chairmanship_manifestoe_poll')
    
    def __str__(self):
        return f'{self.chairmanship}'

        
class State_Rep(models.Model):
    rep = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'state_reps_rep')
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name = 'state_reps_pol_party')
    
    def __str__(self):
        return f'{self.rep.state_reps} (State Representative) ({self.party.name})'
        
class State_House(models.Model):
    state_rep = models.ForeignKey(State_Rep, on_delete=models.CASCADE)
    manifestoe = models.ForeignKey(CandidateManifestoeDetail,on_delete=models.CASCADE, related_name='manifestoe_poll')
    
    def __str__(self):
        return f'{self.state_rep}'

        
class Councilorship(models.Model):
    councilor= models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'councilor_councilorship')
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name = 'councilor_pol_party')
    
    def __str__(self):
        return f'{self.councilor.councilorship} (Ward Councilorship) ({self.party.name})'

class WardCouncilorship(models.Model):
    councilorship = models.ForeignKey(Councilorship, on_delete=models.CASCADE)
    manifestoe = models.ForeignKey(CandidateManifestoeDetail,on_delete=models.CASCADE, related_name='councilorship_manifestoe_poll')
    
    def __str__(self):
        return f'{self.councilorship}'

        