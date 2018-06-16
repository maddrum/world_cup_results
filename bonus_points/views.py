from django.shortcuts import render
from django.views.generic import ListView, CreateView
from bonus_points.models import BonusDescription
from bonus_points.models import BonusUserPrediction
from bonus_points.forms import WorldCupForm


# Create your views here.

class BonusMainListView(ListView):
    template_name = 'bonus_points/bonus-main.html'
    model = BonusDescription
    context_object_name = 'bonuses'

    def get_queryset(self):
        queryset = BonusDescription.objects.filter(bonus_active=True)
        return queryset


class BonusPlayCreateView(CreateView):
    model = BonusUserPrediction
    template_name = 'bonus_points/bonus-input-form.html'
    form_class = WorldCupForm

