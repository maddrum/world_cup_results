from django.shortcuts import render
from django.views.generic import ListView, FormView
from bonus_points.models import BonusDescription, BonusUserPrediction
from bonus_points.forms import SelectAllCountriesForm, InputTextForm
import datetime


# Create your views here.

class BonusMainListView(ListView):
    template_name = 'bonus_points/bonus-main.html'
    context_object_name = 'bonuses'

    def get_queryset(self):
        queryset = BonusUserPrediction.objects.filter(user_bonus_name__bonus_active=True)
        return queryset


class BonusPlayMainView(FormView):
    # get PK from address, check if bonus is active and check if user have not participated
    # writes user prediction to database, or raise error
    # This class must NOT be used alone.
    # It must be inherited with corresponding form_class/according to current data input/

    template_name = 'bonus_points/bonus-input-form.html'
    success_url = "../bonus-main/"

    def form_valid(self, form):
        # input data
        pk = self.kwargs['pk']
        user = self.request.user
        prediction = form.data['user_prediction']
        # data check
        error_check = False
        error_text = ''
        user_count = 0
        time_now = datetime.datetime.utcnow()
        bonus_count = BonusDescription.objects.filter(id=pk, active_until__gt=time_now).count()
        if bonus_count != 0:
            bonus_object = BonusDescription.objects.get(id=pk, active_until__gt=time_now)
            user_count = BonusUserPrediction.objects.filter(user=user, user_bonus_name=bonus_object).count()
        else:
            error_text = 'Този бонус вече не е активен!'
            error_check = True

        if user_count != 0 and bonus_count != 0:
            error_text = 'Вече си в схемата!'
            error_check = True

        if error_check:
            content_dict = {
                'error_text': error_text,
                'show_back_button': False,
            }
            return render(self.request, 'matches/prediction-error.html', content_dict)
        else:
            new_object = BonusUserPrediction(user=user, user_bonus_name=bonus_object, user_prediction=prediction)
            new_object.save()
        return super().form_valid(form)


class AllCountryInputView(BonusPlayMainView):
    form_class = SelectAllCountriesForm


class TextInputView(BonusPlayMainView):
    form_class = InputTextForm
