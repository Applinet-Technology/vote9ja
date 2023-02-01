from django.db import models



class Sector(models.Model):
    name = models.CharField(max_length=50, default='Sector', unique=True)
    
    def __str__(self):
        return self.name

class Manifestoe(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='manifestoe_sector')
    manifestoe_title = models.CharField(max_length=50, unique=True)
    manifestoe = models.TextField(unique=True)
    def __str__(self):
        return f'{self.sector}: {self.manifestoe}'


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
    

class Political_Party(models.Model):
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f'{self.name}'
    

class Presidency(models.Model):
    president = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'presidency_president')
    vice_president = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'presidency_vice_president')
    ruling_party = models.ForeignKey(Political_Party, on_delete=models.CASCADE, related_name = 'presidency_party')
    # manifestoe = models.ForeignKey(Presidential_Manifestoe, on_delete=models.CASCADE, related_name='presidential_manifestoe')
    
    def __str__(self):
        return f'{self.president.presidency} (President) {self.vice_president.presidency} ({self.ruling_party.name})'
        


class Presidential_Manifestoe(models.Model):
    presidency = models.ForeignKey(Presidency, on_delete=models.CASCADE)
    manifestoe = models.ForeignKey(Manifestoe,on_delete=models.CASCADE, related_name='presidency_manifestoe_poll')
    
    def __str__(self):
        return f'{self.manifestoe.manifestoe}'
    

    
class Guber(models.Model):
    governor = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'guber_governor')
    deputy_governor = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'guber_deputy_governor')
    ruling_party = models.ForeignKey(Political_Party, on_delete=models.CASCADE, related_name = 'guber_party')
    
    def __str__(self):
        return f'{self.governor.guber} (Governor) {self.deputy_governor.guber} ({self.ruling_party.name})'
        
class Gubernatorial_Manifestoe(models.Model):
    guber = models.ForeignKey(Guber, on_delete=models.CASCADE)
    manifestoe = models.ForeignKey(Manifestoe,on_delete=models.CASCADE, related_name='guber_manifestoe_poll')
    
    def __str__(self):
        return f'{self.manifestoe.manifestoe}'


class Senate(models.Model):
    senator = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'senate_senator')
    party = models.ForeignKey(Political_Party, on_delete=models.CASCADE, related_name = 'senator_pol_party')
    
    def __str__(self):
        return f'{self.senator.senate} (Senator) ({self.party.name})'
        
class Senatorial_Manifestoe(models.Model):
    senate = models.ForeignKey(Senate, on_delete=models.CASCADE)
    manifestoe = models.ForeignKey(Manifestoe,on_delete=models.CASCADE, related_name='senate_manifestoe_poll')
    
    def __str__(self):
        return f'{self.manifestoe.manifestoe}'

    
        
class Fed_Rep(models.Model):
    rep = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'fed_reps_rep')
    party = models.ForeignKey(Political_Party, on_delete=models.CASCADE, related_name = 'fed_reps_pol_party')
    
    def __str__(self):
        return f'{self.rep.fed_reps} (Federal Representative) ({self.party.name})'

class Fed_Rep_Manifestoe(models.Model):
    rep = models.ForeignKey(Fed_Rep, on_delete=models.CASCADE)
    manifestoe = models.ForeignKey(Manifestoe,on_delete=models.CASCADE, related_name='fedrep_manifestoe_poll')
    
    def __str__(self):
        return f'{self.manifestoe.manifestoe}'
        

class Chairmanship(models.Model):
    chairman = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'chairmanship_chairman')
    vice_chairman= models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'chairmanship_vice_chairman')
    ruling_party = models.ForeignKey(Political_Party, on_delete=models.CASCADE, related_name = 'chairmanship_party')
    
    def __str__(self):
        return f'{self.chairman.chairmanship} (Chairman) {self.vice_chairman.chairmanship} ({self.ruling_party.name})'
class Chairmanship_Manifestoe(models.Model):
    chairmanship = models.ForeignKey(Chairmanship, on_delete=models.CASCADE)
    manifestoe = models.ForeignKey(Manifestoe,on_delete=models.CASCADE, related_name='chairmanship_manifestoe_poll')
    
    def __str__(self):
        return f'{self.manifestoe.manifestoe}'

        
class State_Rep(models.Model):
    rep = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'state_reps_rep')
    ruling_party = models.ForeignKey(Political_Party, on_delete=models.CASCADE, related_name = 'state_reps_pol_party')
    
    def __str__(self):
        return f'{self.rep.state_reps} (State Representative) ({self.ruling_party.name})'
class State_Rep_Manifestoe(models.Model):
    state_rep = models.ForeignKey(State_Rep, on_delete=models.CASCADE)
    manifestoe = models.ForeignKey(Manifestoe,on_delete=models.CASCADE, related_name='manifestoe_poll')
    
    def __str__(self):
        return f'{self.manifestoe.manifestoe}'

        
class Councilorship(models.Model):
    councilor= models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'councilor_councilorship')
    ruling_party = models.ForeignKey(Political_Party, on_delete=models.CASCADE, related_name = 'councilor_pol_party')
    
    def __str__(self):
        return f'{self.councilor.councilorship} (Ward Councilorship) ({self.ruling_party.name})'

class Councilorship_Manifestoe(models.Model):
    councilorship = models.ForeignKey(Councilorship, on_delete=models.CASCADE)
    manifestoe = models.ForeignKey(Manifestoe,on_delete=models.CASCADE, related_name='councilorship_manifestoe_poll')
    
    def __str__(self):
        return f'{self.manifestoe.manifestoe}'

        