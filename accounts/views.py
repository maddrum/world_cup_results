from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts import forms
from matches.models import UserPredictions, Matches, UserScore
from django.contrib.auth.models import User
import datetime


# Create your views here.
class UserRegisterView(CreateView):
    form_class = forms.AccountRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:register_success')


class UserRegisterSuccessView(TemplateView):
    template_name = 'accounts/register-success.html'


class ThankYouView(TemplateView):
    template_name = 'accounts/logout.html'


class UserPredictionsListView(LoginRequiredMixin, ListView):
    model = UserPredictions
    template_name = 'accounts/profile-update-predictions.html'
    context_object_name = 'predictions'

    def get_queryset(self):
        username = self.request.user
        utc_time = datetime.datetime.utcnow()
        utc_time_delta = utc_time + datetime.timedelta(minutes=30)
        queryset = UserPredictions.objects.filter(user_id__username=username,
                                                  match__match_start_time_utc__gte=utc_time_delta)
        return queryset


class UserUpdatePredictionView(LoginRequiredMixin, UpdateView):
    model = UserPredictions
    fields = ('prediction_match_state', 'prediction_goals_home', 'prediction_goals_guest')
    template_name = 'accounts/profile-update-match.html'
    context_object_name = 'update_match'

    def get_queryset(self):
        username = self.request.user
        queryset = super().get_queryset()
        queryset = queryset.filter(user_id__username=username)
        return queryset

    def form_valid(self, form):
        checker = False
        post_data = dict(self.request.POST)
        post_data = {key: value for key, value in post_data.items() if key != "csrfmiddlewaretoken"}
        error_text = ''
        # {'prediction_match_state': ['guest'], 'prediction_goals_home': ['0'], 'prediction_goals_guest': ['2']}
        for key in post_data:
            if key == 'prediction_goals_home' or key == 'prediction_goals_guest':
                try:
                    int(post_data[key][0])
                except ValueError:
                    content_dict = {
                        'error_text': 'Моля, въведете цели положителни числа в полетата за гол! Като бройка голове - един, два, три... Опитай пак!',
                    }
                    return render(self.request, 'matches/prediction-error.html', content_dict)
            goals_home = int(post_data['prediction_goals_home'][0])
            goals_guest = int(post_data['prediction_goals_guest'][0])
            if key == 'prediction_match_state':
                if post_data[key][0] == 'home' and goals_home <= goals_guest:
                    checker = True
                    error_text = 'Головете не съотвестват на въведения изход от двубоя. Въведена е победа за домакин, ' \
                                 'но головете на домакина по-малко от тези на госта!'
                elif post_data[key][0] == 'guest' and goals_guest <= goals_home:
                    checker = True
                    error_text = 'Головете не съотвестват на въведения изход от двубоя. Въведена е победа за гост, ' \
                                 'но головете на госта по-малко от тези на домакина!'
                elif post_data[key][0] == 'tie' and goals_home != goals_guest:
                    checker = True
                    error_text = 'Головете на домакина и на госта не са равни!'
        if checker:
            content_dict = {
                'error_text': error_text,
            }
            return render(self.request, 'matches/prediction-error.html', content_dict)
        else:
            self.object = form.save()
            return super().form_valid(form)


class UserSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('email', 'first_name', 'last_name',)
    template_name = 'accounts/profile-settings.html'
    success_url = '../settings-success'

    def get_object(self, queryset=None):
        username = self.request.user
        queryset = User.objects.get(username=username)
        return queryset


class SettingsSuccess(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile-settings-success.html'


class ProfilePredictionStats(LoginRequiredMixin, ListView):
    model = UserPredictions
    template_name = 'accounts/profile-history-and-points.html'
    context_object_name = 'history'

    def get_queryset(self):
        username = self.request.user
        queryset = UserPredictions.objects.filter(user_id__username=username)
        queryset = queryset.order_by('match')
        return queryset
