from django.conf.urls import url
from main_app import views

app_name = 'main_app'
urlpatterns = [
    url(r'schedule/$', views.Schedule.as_view(), name='schedule'),
    url(r'ranklist/$', views.RankList.as_view(), name='ranklist'),
    url(r'rankilst-detail/(?P<pk>\d+)', views.RankilstUserPoints.as_view(), name='ranklist_detail')
]
