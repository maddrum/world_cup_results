from django.conf.urls import url
from site_stats import views

app_name = 'site_stats'
urlpatterns = [
    url(r'text-stats/$', views.StatsTextStatsView.as_view(), name='text_stats'),
    url(r'prediction-chart/$', views.CommonPredictionChart.as_view(), name='prediction_chart'),
    url(r'points-chart/$', views.CommonPointsChart.as_view(), name='prediction_points'),
    url(r'users-selector/$', views.AllUsersListView.as_view(), name='user_selector'),
    url('predictions-graph-per-user/(?P<pk>\d+)', views.PredictionsGraphPerUser.as_view(),
        name='prediction_graph_per_user'),
    url('points-graph-per-user/(?P<pk>\d+)', views.PointsGraphPerUser.as_view(), name='points_graph_per_user'),
]
