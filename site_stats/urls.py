from django.conf.urls import url
from site_stats import views

app_name = 'site_stats'
urlpatterns = [
    url(r'text-stats/$', views.StatsTextStatsView.as_view(), name='text_stats'),
    url(r'prediction-chart/$', views.prediction_chart, name='prediction_chart'),
]
