from django.views.generic import TemplateView, ListView, DetailView
from matches.models import Matches, UserScore, UserPredictions


class Index(TemplateView):
    template_name = 'main_app/index.html'


class Schedule(ListView):
    template_name = 'main_app/schedule.html'
    model = Matches
    context_object_name = 'schedule'


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
        queryset = UserPredictions.objects.filter(user_id=user_id)
        return queryset
