from django.views.generic import TemplateView


class StatsTextStatsView(TemplateView):
    template_name = 'site_stats/text-stats.html'
