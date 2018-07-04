from django.db import models
from django.contrib.auth import get_user_model
import datetime


class TotalStats(models.Model):
    Users = get_user_model()
    total_predictions = models.IntegerField()
    total_points_gained = models.IntegerField()
    total_match_states_guessed = models.IntegerField()
    total_match_results_guessed = models.IntegerField()
    user_guessed_most_match_states = models.ForeignKey(Users, on_delete=models.CASCADE,
                                                       related_name='stats_user_match_states')
    user_guessed_most_results = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='stats_user_results')
    created_date = models.DateTimeField(default=datetime.datetime.utcnow)
