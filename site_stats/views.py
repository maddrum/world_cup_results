from django.views.generic import TemplateView
from matches.models import UserPredictions


class StatsTextStatsView(TemplateView):
    template_name = 'site_stats/text-stats.html'

    def get_context_data(self, **kwargs):
        # return data from total
        # todo
        context = super().get_context_data()

        return context
