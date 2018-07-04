from matches.models import UserPredictions
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    # calculate total bonus points
    def handle(self, *args, **options):
        # todo
        pass
        self.stdout.write(self.style.SUCCESS('Successfully updated non auto bonuses'))
