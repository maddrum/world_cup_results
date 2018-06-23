from django.views.generic import TemplateView, ListView, CreateView, DetailView
from matches.models import Matches, UserScore, UserPredictions
from main_app.models import SiteContact
from main_app.forms import ContactForm
import datetime


class Index(TemplateView):
    template_name = 'main_app/index.html'


class Schedule(ListView):
    template_name = 'main_app/schedule.html'
    model = Matches
    context_object_name = 'schedule'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        date = datetime.datetime.now().date()
        today_matches = Matches.objects.filter(match_date=date)
        context['today_matches'] = today_matches
        return context


class RankList(ListView):
    template_name = 'main_app/ranklist.html'
    model = UserScore
    context_object_name = 'ranklist'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-points')
        return queryset


class RankilstUserPoints(ListView):
    model = UserPredictions
    template_name = 'main_app/ranklist-detail.html'
    context_object_name = 'ranklist'

    def get_queryset(self):
        user_id = int(self.kwargs['pk'])
        queryset = UserPredictions.objects.filter(user_id=user_id, match__match_is_over=True).order_by(
            '-match__match_start_time_utc')
        return queryset


class SiteContactView(CreateView):
    model = SiteContact
    success_url = '../contact-success'
    template_name = 'main_app/contacts.html'
    form_class = ContactForm


class SiteContactSuccessView(TemplateView):
    template_name = 'main_app/contacts-success.html'


class MatchDetailView(ListView):
    model = UserPredictions
    template_name = 'main_app/match-detail.html'
    context_object_name = 'match'

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = UserPredictions.objects.filter(match__match_number=pk, match__match_is_over=True).order_by('user_id')
        return queryset
