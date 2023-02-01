

from django.contrib import admin

from .models import Poll, FGPoll, StatePoll, Senatorial_districtPoll,Federal_ConstituentPoll, LGAPoll, WardPoll, FGVote, StateVote, Senatorial_districtVote, Federal_ConstituentVote, LGAVote, WardVote, Result



admin.site.register(Poll)

admin.site.register(FGPoll)
admin.site.register(StatePoll)
admin.site.register(Senatorial_districtPoll)
admin.site.register(Federal_ConstituentPoll)
admin.site.register(LGAPoll)
admin.site.register(WardPoll)


admin.site.register(FGVote)
admin.site.register(StateVote)
admin.site.register(Senatorial_districtVote)
admin.site.register(Federal_ConstituentVote)
admin.site.register(LGAVote)
admin.site.register(WardVote)
admin.site.register(Result)
