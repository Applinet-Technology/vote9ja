from django.db import models
from political_parties.parties.manifestoes import MANIFESTOES, MANIFESTOE_DETAILS
from political_parties.parties.inec_parties import REGISTERED_PARTIES
from accounts.models import State, LGA,Senatorial_district,Federal_Constituent, Ward, PollingLocation, User, State_Constituent

from smart_selects.db_fields import ChainedForeignKey



class PoliticalParty(models.Model):
    name = models.CharField(max_length=100, choices=REGISTERED_PARTIES)
    
    @property
    def get_party_name(self):
        return f'{self.get_name_display()}'
        
        
    def __str__(self):
        return self.name
        
class PartyManifestoe(models.Model):
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name='partymanifestos')
    manifestoe=models.CharField(max_length=250, choices=MANIFESTOES)
    source = models.URLField(max_length=200)
    def __str__(self):
        return f'{self.get_manifestoe_display()}'
        

class PartyManifestoeDetail(models.Model):
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name='political_party_manifesto_detail')
    manifestoe= ChainedForeignKey(PartyManifestoe,
        chained_field="party",
        chained_model_field="party",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )

    # manifestoe = models.ForeignKey(PartyManifestoe, on_delete=models.CASCADE,related_name='political_party_manifesto')
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
 



class Presidency(models.Model):
    president = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'presidency_president')
    vice_president = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'presidency_vice_president')
    def __str__(self):
        return f'{self.president.presidency} (President) {self.vice_president.presidency}'
        
class PresidencyParty(models.Model):
    presidency = models.ForeignKey(Presidency, on_delete=models.CASCADE, related_name = 'presidency_party_party')
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name = 'presidency_party')
    
    property
    def get_party_name(self):
        return f'{self.party.get_name_display()}'
    
    def __str__(self):
        return self.party.name
        
class PresidencyCandidateManifestoe(models.Model):
    presidency=models.ForeignKey(Presidency, on_delete=models.CASCADE, related_name='Presidencycand')
    manifestoe = models.CharField(max_length=200)
    source = models.URLField(max_length=200)
    
    def __str__(self):
        return f'{self.manifestoe}'

class PresidencyCandidateManifestoeDetail(models.Model):
    presidency=models.ForeignKey(Presidency, on_delete=models.CASCADE, related_name='Presidencycanddetals')
    
    manifestoe= ChainedForeignKey(PresidencyCandidateManifestoe,
        chained_field="presidency",
        chained_model_field="presidency",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
        
    # manifestoe = models.ForeignKey(PresidencyCandidateManifestoe, on_delete=models.CASCADE, related_name='candidate_manifestoe_politician')
    detail = models.TextField(unique=True)
    def __str__(self):
        return f'{self.detail}'

class Presidential(models.Model):
    presidency = models.ForeignKey(Presidency, on_delete=models.CASCADE)
    
    manifestoe= ChainedForeignKey(PresidencyCandidateManifestoe,
        chained_field="presidency",
        chained_model_field="presidency",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )

    
    
    
    # manifestoe = models.ForeignKey(PresidencyCandidateManifestoeDetail,on_delete=models.CASCADE, related_name='presidential_manifestoe_poll')
    
    def __str__(self):
        return f'{self.manifestoe.manifestoe}'

    
class Guber(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name = 'state_guber_governor')
    governor = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'guber_governor')
    deputy_governor = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'guber_deputy_governor')
    def __str__(self):
        return f'{self.governor.guber} (Governor) {self.deputy_governor.guber}'

class GParty(models.Model):
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name = 'guber_party', default=1)
    def __str__(self):
        return self.party.get_name_display()

    
    
class GuberParty(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name = 'state_guber_governor_party')
    guber= ChainedForeignKey(Guber,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # guber = models.ForeignKey(Guber, on_delete=models.CASCADE, related_name = 'chain_guber_party')
    party = models.ForeignKey(GParty, on_delete=models.CASCADE, related_name = 'gparty_party', default=1)
    
    def __str__(self):
        return self.party.party.get_name_display()
        
        
        
class GuberCandidateManifestoe(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name = 'state_guber_governor_mandetails')
    
    guber= ChainedForeignKey(Guber,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    #guber=models.ForeignKey(Guber, on_delete=models.CASCADE, related_name='gubercand')
    manifestoe = models.CharField(max_length=200)
    source = models.URLField(max_length=200)
    
    def __str__(self):
        return f'{self.manifestoe}'

class GuberCandidateManifestoeDetail(models.Model):
    state=models.ForeignKey(State, on_delete=models.CASCADE, related_name='stategubercanddetals')
    
    guber= ChainedForeignKey(Guber,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # guber=models.ForeignKey(Guber, on_delete=models.CASCADE, related_name='gubercanddetals')
    
    manifestoe= ChainedForeignKey(GuberCandidateManifestoe,
        chained_field="guber",
        chained_model_field="guber",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
        
    # manifestoe = models.ForeignKey(PresidencyCandidateManifestoe, on_delete=models.CASCADE, related_name='candidate_manifestoe_politician')
    detail = models.TextField(unique=True)
    def __str__(self):
        return f'{self.detail}'

        
class Gubernatorial(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name = 'state_guber_governor_mandetailsgh')
    
    guber= ChainedForeignKey(Guber,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # guber = models.ForeignKey(Guber, on_delete=models.CASCADE)
    manifestoe= ChainedForeignKey(GuberCandidateManifestoe,
        chained_field="guber",
        chained_model_field="guber",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # manifestoe = models.ForeignKey(GuberCandidateManifestoeDetail,on_delete=models.CASCADE, related_name='guber_manifestoe_poll')
    
    def __str__(self):
        return f'{self.guber}'


class Senate(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='senatorial_distrsct_senate_state_con_candidate', default=1)
    senDis= ChainedForeignKey(Senatorial_district,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # senDis= models.ForeignKey(Senatorial_district, on_delete=models.CASCADE, related_name = 'senatorial_district_senate')
    senator = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'senate_senator')
    def __str__(self):
        return f'{self.senator.senate} (Senator)'
    
class SenateParty(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='senatorial_distrsct_senate_state_candidate', default=1)
    senDis= ChainedForeignKey(Senatorial_district,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    senate= ChainedForeignKey(Senate,
        chained_field="senDis",
        chained_model_field="senDis",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name = 'senator_pol_party')
    
    def __str__(self):
        return f'{self.senate.senator} (Senator) ({self.party.get_name_display()})'
        
class SenateCandidateManifestoe(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='senatorial_distrsct_senate_state_con_candidate_manifestoe', default=1)
    senDis= ChainedForeignKey(Senatorial_district,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    # senate= ChainedForeignKey(Senate,
    #     chained_field="senDis",
    #     chained_model_field="senator",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True,
    #     )
    # # senate=models.ForeignKey(Senate, on_delete=models.CASCADE, related_name='senatecand')
    manifestoe = models.CharField(max_length=200)
    source = models.URLField(max_length=200)
    
    def __str__(self):
        return f'{self.manifestoe}'

class SenateCandidateManifestoeDetail(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='senatorial_distrsct_senate_state_con_candidate_manifestoe_detail', default=1)
    senDis= ChainedForeignKey(Senatorial_district,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # senate= ChainedForeignKey(Senate,
    #     chained_field="senDis",
    #     chained_model_field="senDis",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True,
    #     )
    
    manifestoe= ChainedForeignKey(SenateCandidateManifestoe,
        chained_field="senDis",
        chained_model_field="senDis",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
        
    # manifestoe = models.ForeignKey(PresidencyCandidateManifestoe, on_delete=models.CASCADE, related_name='candidate_manifestoe_politician')
    detail = models.TextField(unique=True)
    def __str__(self):
        return f'{self.detail}'

        
class Senatorial(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='senatorial_distrsct_senatorial_state_candidate_manifestoe_detail', default=1)
    senDis= ChainedForeignKey(Senatorial_district,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # senate= ChainedForeignKey(Senate,
    #     chained_field="senDis",
    #     chained_model_field="senDis",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True,
    #     )
    manifestoe= ChainedForeignKey(SenateCandidateManifestoe,
        chained_field="senDis",
        chained_model_field="senDis",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
        
    detail= ChainedForeignKey(SenateCandidateManifestoeDetail,
        chained_field="manifestoe",
        chained_model_field="manifestoe",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        default=1
        )
        
    # senate = models.ForeignKey(Senate, on_delete=models.CASCADE)
    # details = models.ForeignKey(SenateCandidateManifestoeDetail,on_delete=models.CASCADE, related_name='senate_manifestoe_poll')
    
    def __str__(self):
        return f'{self.detail}'

    
        
class Fed_Rep(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='fedcon_rep_lga_rep_con_candidate', default=1)
    fedCon= ChainedForeignKey(Federal_Constituent,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # fedCon = models.ForeignKey(Federal_Constituent, on_delete=models.CASCADE, related_name='fedcon_rep_state')
    rep = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'fed_reps_rep')
    def __str__(self):
        return f'{self.rep.fed_reps} (Federal Representative)'

class Fed_RepParty(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='fedcon_rep_party_candidate',default=1)
    fedCon= ChainedForeignKey(Federal_Constituent,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    rep= ChainedForeignKey(Fed_Rep,
        chained_field="fedCon",
        chained_model_field="fedCon",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name = 'fed_reps_pol_party')
    
    def __str__(self):
        return f' (Federal Representative) ({self.party.get_name_display()})'
        
        
class Fed_RepCandidateManifestoe(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_fed_rep_con_candidate_manifestoe',default=1)
    fedCon= ChainedForeignKey(Federal_Constituent,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    rep= ChainedForeignKey(Fed_Rep,
        chained_field="fedCon",
        chained_model_field="fedCon",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # party= ChainedForeignKey(Fed_RepParty,
    #     chained_field="rep",
    #     chained_model_field="fedCon",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True,
    #     )
    manifestoe = models.CharField(max_length=200)
    source = models.URLField(max_length=200)
    
    def __str__(self):
        return f'{self.manifestoe}'

class Fed_RepCandidateManifestoeDetail(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_fed_rep_con_candidate_manifestoe_details', default=1)
    fedCon= ChainedForeignKey(Federal_Constituent,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    rep= ChainedForeignKey(Fed_Rep,
        chained_field="fedCon",
        chained_model_field="fedCon",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # party= ChainedForeignKey(Fed_RepParty,
    #     chained_field="rep",
    #     chained_model_field="fedCon",
    #     show_all=False, 
    #     auto_choose=True, 
    #     sort=True,
    #     )
    # rep=models.ForeignKey(Fed_Rep, on_delete=models.CASCADE, related_name='fedrepcanddetals')
    
    manifestoe= ChainedForeignKey(Fed_RepCandidateManifestoe,
        chained_field="rep",
        chained_model_field="fedCon",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
        
    # manifestoe = models.ForeignKey(PresidencyCandidateManifestoe, on_delete=models.CASCADE, related_name='candidate_manifestoe_politician')
    detail = models.TextField(unique=True)
    def __str__(self):
        return f'{self.detail}'


class Fed_House(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='senatorial_dist_senatorial_state_candidate_manifestoe_detail', default=1)
    fedCon= ChainedForeignKey(Federal_Constituent,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    rep= ChainedForeignKey(Fed_Rep,
        chained_field="fedCon",
        chained_model_field="fedCon",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    manifestoe= ChainedForeignKey(Fed_RepCandidateManifestoeDetail,
        chained_field="rep",
        chained_model_field="rep",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # manifestoe = models.ForeignKey(Fed_RepCandidateManifestoeDetail,on_delete=models.CASCADE, related_name='fedrep_manifestoe_poll')
    
    def __str__(self):
        return f'{self.manifestoe.detail}'
        

class Chairmanship(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_lga_chairmanship_candidate')
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    # lga = models.ForeignKey(LGA, on_delete=models.CASCADE, related_name='lga_chairman_chairmanship_chair')
    chairman = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'chairmanship_chairman')
    vice_chairman= models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'chairmanship_vice_chairman')
    def __str__(self):
        return f'{self.chairman.chairmanship} (Chairman) {self.vice_chairman.chairmanship}'


class ChairmanshipParty(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_chairmanship_candidate')
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    chairmanship= ChainedForeignKey(Chairmanship,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name = 'chairmanship_party')
    
    def __str__(self):
        return f'{self.chairmanship.chairman.chairmanship} (Chairman) {self.chairmanship.vice_chairman.chairmanship} ({self.party})'

class ChairmanshipCandidateManifestoe(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_lga_rep_chairmanship_candidate_manifestoe')
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # lga = models.ForeignKey(LGA, on_delete=models.CASCADE, related_name='lag_chairmanship_chair_candidate')
    
    chairmanship= ChainedForeignKey(Chairmanship,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    #chairmanship=models.ForeignKey(Chairmanship, on_delete=models.CASCADE, related_name='chairmanshipcand', default=1)
    manifestoe = models.CharField(max_length=200)
    source = models.URLField(max_length=200)
    
    def __str__(self):
        return f'{self.manifestoe}'

class ChairmanshipCandidateManifestoeDetail(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_lga_chhairmanship_candidate_man_detaiks')
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # lga = models.ForeignKey(LGA, on_delete=models.CASCADE, related_name='lga_candidate_chairmanship_chair_candidate')
    
    chairmanship= ChainedForeignKey(Chairmanship,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    
    manifestoe= ChainedForeignKey(ChairmanshipCandidateManifestoe,
        chained_field="chairmanship",
        chained_model_field="chairmanship",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
        
    # manifestoe = models.ForeignKey(PresidencyCandidateManifestoe, on_delete=models.CASCADE, related_name='candidate_manifestoe_politician')
    detail = models.TextField(unique=True)
    def __str__(self):
        return f'{self.detail}'

        
class LGAChairmanship(models.Model):
    chairmanship = models.ForeignKey(Chairmanship, on_delete=models.CASCADE)
    manifestoe = models.ForeignKey(ChairmanshipCandidateManifestoeDetail,on_delete=models.CASCADE, related_name='chairmanship_manifestoe_poll')
    
    def __str__(self):
        return f'{self.manifestoe.detail}'

        
class State_Rep(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_rep_candidate_manifestoe')
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    stateCon= ChainedForeignKey(State_Constituent,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )

    rep = models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'state_reps_rep')
    def __str__(self):
        return f'{self.rep.state_reps} (State Representative)'
    
class State_RepParty(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_rep_party_candidate_manifestoe')
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    stateCon= ChainedForeignKey(State_Constituent,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    rep= ChainedForeignKey(State_Rep,
        chained_field="stateCon",
        chained_model_field="stateCon",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name = 'state_reps_pol_party')
    
    def __str__(self):
        return f'{self.rep.rep.state_reps} (State Representative) ({self.party.get_name_display()})'
        
class State_RepCandidateManifestoe(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_rep_con_candidate_manifestoe')
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    stateCon= ChainedForeignKey(State_Constituent,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    rep= ChainedForeignKey(State_Rep,
        chained_field="stateCon",
        chained_model_field="stateCon",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # rep=models.ForeignKey(State_Rep, on_delete=models.CASCADE, related_name='staterepcand')
    manifestoe = models.CharField(max_length=200)
    source = models.URLField(max_length=200)
    
    def __str__(self):
        return f'{self.manifestoe}'

class State_RepCandidateManifestoeDetail(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_rep_con_candidate_details',default=1)
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    stateCon= ChainedForeignKey(State_Constituent,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    rep= ChainedForeignKey(State_Rep,
        chained_field="stateCon",
        chained_model_field="stateCon",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # rep=models.ForeignKey(State_Rep, on_delete=models.CASCADE, related_name='staterepcanddetals')
    
    manifestoe= ChainedForeignKey(State_RepCandidateManifestoe,
        chained_field="rep",
        chained_model_field="rep",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    detail = models.TextField(unique=True)
    def __str__(self):
        return f'{self.detail}'

        
class State_House(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_rep_con_candidate_house', default=1)
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    stateCon= ChainedForeignKey(State_Constituent,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    rep= ChainedForeignKey(State_Rep,
        chained_field="stateCon",
        chained_model_field="stateCon",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # rep=models.ForeignKey(State_Rep, on_delete=models.CASCADE, related_name='staterepcanddetals')
    
    manifestoe= ChainedForeignKey(State_RepCandidateManifestoe,
        chained_field="rep",
        chained_model_field="rep",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    def __str__(self):
        return f'{self.rep}'

        
class Councilorship(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='councilor_councilorship_rep_con_cand')
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    ward= ChainedForeignKey(Ward,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    councilor= models.ForeignKey(Politician, on_delete=models.CASCADE, related_name = 'councilor_councilorship')
    def __str__(self):
        return f'{self.councilor.councilorship} (Ward Councilorship)'
    
class CouncilorshipParty(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_councilor_councilorship_rep_con_cand')
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    ward= ChainedForeignKey(Ward,
        chained_field="lga",
        chained_model_field="lga",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    councilorship= ChainedForeignKey(Councilorship,
        chained_field="ward",
        chained_model_field="ward",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    party = models.ForeignKey(PoliticalParty, on_delete=models.CASCADE, related_name = 'councilor_pol_party')
    
    def __str__(self):
        return f'{self.councilorship.councilor.councilorship} (Ward Councilorship) ({self.party.get_name_display()})'
        
class CouncilorshipCandidateManifestoe(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='councilorship_state_rep_con_cand')
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    ward= ChainedForeignKey(Ward,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    councilorship= ChainedForeignKey(Councilorship,
        chained_field="ward",
        chained_model_field="ward",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # councilorship=models.ForeignKey(Councilorship, on_delete=models.CASCADE, related_name='councilorshipcand')
    manifestoe = models.CharField(max_length=200)
    source = models.URLField(max_length=200)
    
    def __str__(self):
        return f'{self.manifestoe}'

class CouncilorshipCandidateManifestoeDetail(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_coun_lga_con_cand')
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    ward= ChainedForeignKey(Ward,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    councilorship= ChainedForeignKey(Councilorship,
        chained_field="ward",
        chained_model_field="ward",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # councilorship=models.ForeignKey(Councilorship, on_delete=models.CASCADE, related_name='councilorshipcanddetals')
    
    manifestoe= ChainedForeignKey(CouncilorshipCandidateManifestoe,
        chained_field="councilorship",
        chained_model_field="councilorship",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
        
    # manifestoe = models.ForeignKey(PresidencyCandidateManifestoe, on_delete=models.CASCADE, related_name='candidate_manifestoe_politician')
    detail = models.TextField(unique=True)
    def __str__(self):
        return f'{self.detail}'


class WardCouncilorship(models.Model):
    state= models.ForeignKey(State, on_delete=models.CASCADE, related_name='state_coun_lga_con_candidacy',default=1)
    lga= ChainedForeignKey(LGA,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    ward= ChainedForeignKey(Ward,
        chained_field="state",
        chained_model_field="state",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    councilorship= ChainedForeignKey(Councilorship,
        chained_field="ward",
        chained_model_field="ward",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
    # councilorship=models.ForeignKey(Councilorship, on_delete=models.CASCADE, related_name='councilorshipcanddetals')
    
    manifestoe= ChainedForeignKey(CouncilorshipCandidateManifestoe,
        chained_field="councilorship",
        chained_model_field="councilorship",
        show_all=False, 
        auto_choose=True, 
        sort=True,
        )
        
    # councilorship = models.ForeignKey(Councilorship, on_delete=models.CASCADE)
    # manifestoe = models.ForeignKey(CouncilorshipCandidateManifestoeDetail,on_delete=models.CASCADE, related_name='councilorship_manifestoe_poll')
    
    def __str__(self):
        return f'{self.manifestoe.manifestoe}{self.councilorship.councilor.councilorship}'

        