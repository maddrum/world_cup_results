from django import template
from bonus_points.models import BonusDescription
import datetime

register = template.Library()


@register.simple_tag
def active_bonuses_checker():
    current_time = datetime.datetime.now()
    all_bonuses = BonusDescription.objects.filter(active_until__gte=current_time, archived=False,
                                                  bonus_active=True).count()
    if all_bonuses != 0:
        return True
    else:
        return False
