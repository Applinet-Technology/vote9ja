

from django.contrib import admin

from .models import Sector, Manifestoe, Poll, FederalPoll, StatePoll, Senatorial_districtPoll,Federal_ConstituentPoll, LGAPoll, WardPoll,Result


admin.site.register(Sector)
admin.site.register(Manifestoe)
admin.site.register(Poll)

@admin.register(FederalPoll)
class FederalPollAdmin(admin.ModelAdmin):
    list_display = ( "voter","poll", "choice", "vote_date", "has_voted",)
    list_filter = ("poll__manifestoe__sector", "choice", "vote_date", "has_voted")
    search_fields = ("poll__manifestoe__sector", "has_voted", "vote_date",)
    
    
admin.site.register(StatePoll)
admin.site.register(Senatorial_districtPoll)
admin.site.register(Federal_ConstituentPoll)
admin.site.register(LGAPoll)
admin.site.register(WardPoll)
admin.site.register(Result)