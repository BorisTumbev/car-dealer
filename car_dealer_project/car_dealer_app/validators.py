import datetime
from django.core.exceptions import ValidationError


def curr_year_validator(value):
    """
    validator for Year property of a Vehicle
    """
    if value < 1855 or value > datetime.datetime.now().year:
        raise ValidationError('ensure value is between 1855 and current year!',params={'value': value},)

def curr_day_validator(value):
    """
    validator for Rented until property of a rental Vehicle
    """
    if value <= datetime.datetime.now(value.tzinfo) :
        raise ValidationError(('day {} is in the past!').format(value),params={'value': value},)