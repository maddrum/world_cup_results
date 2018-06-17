from django.conf.urls import url
from bonus_points import views

app_name = 'bonus_points'
urlpatterns = [
    url(r'bonus-main/$', views.BonusMainListView.as_view(), name='bonus_main'),
    url(r'text/(?P<pk>\d+)$', views.TextInputView.as_view(), name='bonus_input'),
    url(r'country/(?P<pk>\d+)$', views.AllCountryInputView.as_view(), name='bonus_input'),

]
