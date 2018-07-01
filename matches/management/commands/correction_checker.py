from django.core.management.base import BaseCommand
from matches.models import UserPredictions
import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        all_predictions = UserPredictions.objects.all()
        for item in all_predictions:
            time_delta_creation_last_edit = item.last_edit - item.creation_time
            if time_delta_creation_last_edit.seconds != 0:
                print('--------------------------------------')
                print(item)
                print(f'created: {item.creation_time}')
                print(f'edited: {item.last_edit}')
                print(f'Time Delta: {time_delta_creation_last_edit}')

        self.stdout.write(self.style.SUCCESS('all corrections were displayed'))
