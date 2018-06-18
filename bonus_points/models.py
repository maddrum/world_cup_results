from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class BonusDescription(models.Model):
    # each bonus must have only one correct answer.
    input_choices = [('text', 'text'), ('number', 'number'), ('all-countries', 'all-countries')]
    bonus_name = models.CharField(max_length=200)
    active_until = models.DateTimeField()
    correct_answer = models.CharField(max_length=500, null=True, blank=True)
    points = models.IntegerField()
    participate_link = models.BooleanField(default=False)
    #all users automatically apply for bonuses with participate_link = False.
    bonus_active = models.BooleanField(default=False)
    input_filed = models.CharField(max_length=20, default='text', choices=input_choices)
    archived = models.BooleanField(default=False)

    # only active bonuses will be shown not active bonuses are just a drafts

    def __str__(self):
        return str(self.bonus_name) + ' и вземи ' + str(self.points) + ' точки'


class BonusUserPrediction(models.Model):
    # users store their bonus score answers
    user_model = get_user_model()
    user_bonus_name = models.ForeignKey(BonusDescription, on_delete=models.CASCADE, related_name='user_bonus_name')
    user = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name='bonus_user')
    user_prediction = models.CharField(max_length=500)
    points_gained = models.IntegerField(default=0)
    summary_text = models.CharField(max_length=500)
    user_participate = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user) + ' ' + str(self.user_bonus_name)


class UserBonusSummary(models.Model):
    user_model = get_user_model()
    user = models.ForeignKey(user_model, on_delete=models.CASCADE, related_name="user_bonus")
    total_bonus_points = models.IntegerField()
    total_summary = models.TextField()

    def __str__(self):
        return str(self.user)
