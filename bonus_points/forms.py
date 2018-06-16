from django import forms
from bonus_points.models import BonusUserPrediction
from matches.models import Countries
from django.forms.widgets import Select


class WorldCupForm(forms.ModelForm):
    # for champion prediction
    class Meta:
        countries = [(item.name, item.name) for item in Countries.objects.all()]
        model = BonusUserPrediction
        fields = ('user_prediction',)
        widgets = {
            'user_prediction': Select(choices=countries)
        }
