from django.core.exceptions import ValidationError

from edc_base.utils import get_utcnow


def datetime_not_now(value):
    if value == get_utcnow():
        raise ValidationError('Cannot be current date and time')


def date_not_now(value):
    if value == get_utcnow().date():
        raise ValidationError('Cannot be today\'s date')