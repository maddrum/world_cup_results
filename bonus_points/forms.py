from django import forms
from matches.models import Countries
from django.forms.widgets import Select


class SelectAllCountriesForm(forms.Form):
    # def __init__(self, countries_list):
    #     if countries_list == 'all':
    #         self.countries_list = [(item.name, item.name) for item in Countries.objects.all()]
    #     else:
    #         self.countries_list = [(item, item) for item in countries_list]
    #     super().__init__()

    countries = [(item.name, item.name) for item in Countries.objects.all()]
    user_prediction = forms.CharField(widget=Select(choices=countries), label='Избери държава')


class InputTextForm(forms.Form):
    user_prediction = forms.CharField(label='Напиши твоята прогноза')



class InputNumberForm(forms.Form):
    user_prediction = forms.IntegerField(label='Въведи номер')
