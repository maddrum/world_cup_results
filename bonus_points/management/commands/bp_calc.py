from bonus_points.models import BonusUserPrediction
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    #calculate bonus points for contest "give prediction for 36 matches" /id = 1/
    def handle(self, *args, **options):

        user_predictions = BonusUserPrediction.objects.all()
        for item in user_predictions:
            print(item)

        self.stdout.write(self.style.SUCCESS('Successfully printed!'))
