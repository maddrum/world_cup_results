from django.conf.urls import url
from bonus_points import views

app_name = 'bonus_points'
urlpatterns = [
    url(r'bonus-main', views.BonusMainListView.as_view(), name='bonus_main'),
]
