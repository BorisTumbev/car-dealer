
from django.core.paginator import Paginator
import datetime
from django.core.exceptions import ValidationError
from django.core.mail import send_mail

#current date for "created at" property in Vehicle model
def curr_year_validator(value):
    if value < 1855 or value > datetime.datetime.now().year:
        raise ValidationError(('year {} is in the future!').format(value),params={'value': value},)

def curr_day_validator(value):
    if value <= datetime.datetime.now(value.tzinfo) :
        raise ValidationError(('day {} is in the past!').format(value),params={'value': value},)


def pagination(request,object_list):
    """
    function for making pages
    """

    paginator = Paginator(object_list, 10)

    page = request.GET.get('page')
    limited_obj = paginator.get_page(page)
    return limited_obj

def mail_send(msg):

    send_mail(subject='Selling request',message=msg,from_email='test.mycode9999@gmail.com',recipient_list=['test.mycode9999@gmail.com'],fail_silently=False,)


"""
field choices for the models
"""

users_roles =(
    ('SRA','Sales_rent_agent'),
    ('SA','Sales_agent'),
    ('RA','Rental_agent')
)

conditions = (
    ('N','New'),
    ('U','Used')
)

transmission_types = (
    ('A','Auto'),
    ('M','Manual'),
    ('S','Semi-auto')
) 

engine_types = (
    ('D','Disel'),
    ('P','Petrol'),
    ('E','Electric'),
    ('H','Hybrid')
)

vehicle_types = (
    ('A','Automobile'),
    ('M','Motorcycle'),
    ('B','Bus'),
    ('T','Truck')
)

sell_status = (
    ('A','Active'),
    ('S','Sold'),
    ('P','Pending'),
    ('N','Neutral')
)
