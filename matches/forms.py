from django.forms import ModelForm
from matches.models import UserPredictions


class InputDailyPredictionForm(ModelForm):
    class Meta:
        model = UserPredictions
        fields = ['prediction_match_state', 'prediction_goals_home', 'prediction_goals_guest']
