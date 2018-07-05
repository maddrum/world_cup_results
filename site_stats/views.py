from django.views.generic import TemplateView
from site_stats.models import TotalStats, UserGuessesNumber
from matches.models import UserPredictions
from matches.models import EventDates
from django.utils import timezone
import datetime
# for fussion charts
from fusioncharts.fusioncharts import FusionCharts


class StatsTextStatsView(TemplateView):
    template_name = 'site_stats/text-stats.html'

    def get_context_data(self, **kwargs):
        # return data from total
        context = super().get_context_data()
        all_stats = TotalStats.objects.all().order_by('-created_date')
        user_most_match_states = UserGuessesNumber.objects.all().order_by('-guessed_matches')[0]
        user_most_results = UserGuessesNumber.objects.all().order_by('-guessed_results')[0]
        latest_stats = all_stats[0]
        # convert created date into Sofia time
        timezone_sofia = timezone.get_default_timezone()
        utc_created_time = timezone.utc.localize(latest_stats.created_date, is_dst=None)
        sofia_created_time = utc_created_time.astimezone(timezone_sofia)
        # add some context
        context['total_predicioons'] = latest_stats.total_predictions
        context['total_points_gained'] = latest_stats.total_points_gained
        context['total_match_states_guessed'] = latest_stats.total_match_states_guessed
        context['total_match_results_guessed'] = latest_stats.total_match_results_guessed
        context['date'] = sofia_created_time
        context['user_most_match_states'] = user_most_match_states
        context['user_most_results'] = user_most_results

        return context


class CommonPredictionChart(TemplateView):
    template_name = 'site_stats/stats-predictions.html'

    def get_context_data(self, **kwargs):
        all_events = EventDates.objects.all()
        event_dates = {item.event_name: [item.event_start_date, item.event_end_date,
                                         (item.event_end_date - item.event_start_date).days] for item in
                       all_events}

        context = super().get_context_data()
        data_source = {}
        data_source['chart'] = {
            "xAxisName": "Ден",
            "yAxisName": "Брой дадени прогнози",
            "theme": "zune"
        }
        data_source['data'] = []
        for item in event_dates.values():
            start_date = item[0]
            end_date = item[1]
            difference = item[2]
            for day in range(difference + 1):
                query_date = start_date + datetime.timedelta(days=day)
                day_prediction_count = UserPredictions.objects.filter(match__match_date=query_date).count()
                temp_dict = {
                    "label": str(query_date),
                    "value": day_prediction_count,
                }
                data_source['data'].append(temp_dict)

        column2d = FusionCharts("column2d", "ex1", "600", "400", "chart-1", "json", data_source)
        context['output'] = column2d.render().encode('utf-8').decode('utf-8')
        return context
