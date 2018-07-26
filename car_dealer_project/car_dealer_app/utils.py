
from django.core.paginator import Paginator
import datetime


def pagination(request,object_list):
    """
    function for making pages
    """

    paginator = Paginator(object_list, 10)

    page = request.GET.get('page')
    limited_obj = paginator.get_page(page)
    return limited_obj


#current date for "created at" property in Vehicle model
curr_year = datetime.datetime.now().year

"""
field choices for the models
"""

conditions         = (
                ('N','New'),
                ('U','Used')
                    )

transmission_types = (
                ('A','Auto'),
                ('M','Manual'),
                ('S','Semi-auto')
                    ) 

engine_types       = (
                ('D','Disel'),
                ('P','Petrol'),
                ('E','Electric'),
                ('H','Hybrid')
                    )

vehicle_types      = (
                ('A','Automobile'),
                ('M','Motorcycle'),
                ('B','Bus'),
                ('T','Truck')
                     )

sell_status        = (
                ('A','Active'),
                ('S','Sold'),
                ('P','Pending'),
                ('N','Neutral')
                    )
