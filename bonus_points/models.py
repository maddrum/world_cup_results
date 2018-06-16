from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class BonusDescription(models.Model):
    # each bonus must have only one correct answer.
    bonus_name = models.CharField(max_length=200)
    active_until = models.DateTimeField()
    correct_answer = models.CharField(max_length=500, null=True)
    points = models.IntegerField()
    participate_link = models.BooleanField(default=False)
    # only active bonuses will be calculated. Bonus will become active when answer is known - ex Bonus question
    bonus_active = models.BooleanField(default=False)


class BonusUserPrediction(models.Model):
    # users store their bonus score answers
    user_model = get_user_model()
    user_bonus_name = models.ForeignKey(BonusDescription, on_delete=models.CASCADE, related_name='user_bonus_name')
    user = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name='bonus_user')
    user_prediction = models.CharField(max_length=500)
    points_gained = models.IntegerField(default=0)
    summary_text = models.CharField(max_length=500)


class UserBonusSummary(models.Model):
    user_model = get_user_model()
    user = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name="user_bonus")
    total_bonus_points = models.IntegerField()
    total_summary = models.TextField()
