

from django.contrib import admin
from .models import State, LGA,Senatorial_district,Federal_Constituent, Ward, PollingLocation, User, State_Constituent

admin.site.register(State)
admin.site.register(LGA)
admin.site.register(State_Constituent)
admin.site.register(PollingLocation)
admin.site.register(Ward)
admin.site.register(User)
admin.site.register(Senatorial_district)
admin.site.register(Federal_Constituent)
#admin.site.register(Result)
