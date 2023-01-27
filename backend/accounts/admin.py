


from django.contrib import admin
from .models import State, LGA,Senatorial_district,Federal_Constituent, Ward, User,Category, Blog, Sector, Manifestoe, FederalPoll, StatePoll, Senatorial_districtPoll,Federal_ConstituentPoll, LGAPoll, Result


admin.site.register(State)
admin.site.register(LGA)
admin.site.register(Senatorial_districtPoll)
admin.site.register(Federal_ConstituentPoll)
admin.site.register(Ward)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Sector)
admin.site.register(Manifestoe)

@admin.register(FederalPoll)
class FederalPollAdmin(admin.ModelAdmin):
    list_display = ( "manifestoe", "choice", "vote_date", "has_voted",)
    list_filter = ("manifestoe__sector", "choice", "vote_date", "has_voted")
    search_fields = ("manifestoe__sector", "has_voted", "vote_date",)
    
    
admin.site.register(StatePoll)
admin.site.register(LGAPoll)
admin.site.register(Senatorial_district)
admin.site.register(Federal_Constituent)
admin.site.register(Result)
