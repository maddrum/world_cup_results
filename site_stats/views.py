from django.views.generic import TemplateView
from site_stats.models import TotalStats, UserGuessesNumber
from django.utils import timezone
# for fussion charts
from django.shortcuts import render
from django.http import HttpResponse
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


def prediction_chart(request):
    column2d = FusionCharts("column2d", "ex1", "600", "400", "chart-1", "json",
                            """{  
                            "chart": {                                              
                                "xAxisName": "Ден",
                                "yAxisName": "Брой дадени прогнози",                                
                                "theme": "zune"
                                
                            },
                            "data": [{
                                "label": "Jan",
                                "value": "420000"
                            }, {
                                "label": "Feb",
                                "value": "810000"
                            }, {
                                "label": "Mar",
                                "value": "720000"
                            }, {
                                "label": "Apr",
                                "value": "550000"
                            }, {
                                "label": "May",
                                "value": "910000"
                            }, {
                                "label": "Jun",
                                "value": "510000"
                            }, {
                                "label": "Jul",
                                "value": "680000"
                            }, {
                                "label": "Aug",
                                "value": "620000"
                            }, {
                                "label": "Sep",
                                "value": "610000"
                            }, {
                                "label": "Oct",
                                "value": "490000"
                            }, {
                                "label": "Nov",
                                "value": "900000"
                            }, {
                                "label": "Dec",
                                "value": "730000"
                            }]
                        }""")
    request.encoding = 'UTF-8'
    return render(request, 'site_stats/stats-predictions.html', {'output': column2d.render().encode('utf-8').decode('utf-8')})
