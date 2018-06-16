from django.shortcuts import render
from django.views.generic import ListView
from bonus_points.models import BonusDescription


# Create your views here.

class BonusMainListView(ListView):
    template_name = 'bonus_points/bonus-main.html'
    model = BonusDescription
    context_object_name = 'bonuses'

    def get_queryset(self):
        queryset = BonusDescription.objects.filter(bonus_active=True)
