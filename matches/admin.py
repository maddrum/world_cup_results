from django.contrib import admin
from matches.models import Countries, Matches, UserPredictions, UserScore

admin.site.register(Countries)
admin.site.register(Matches)
admin.site.register(UserPredictions)
admin.site.register(UserScore)
