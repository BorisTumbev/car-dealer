#from enum import Enum
import datetime
from django.core.paginator import Paginator


def pagination(request,object_list):
    paginator = Paginator(object_list, 2)

    page = request.GET.get('page')
    limited_obj = paginator.get_page(page)
    return limited_obj



curr_year = datetime.datetime.now().year


conditions         = (('N','New'),
                      ('U','Used'))

transmission_types = (('A','Auto'),
                      ('M','Manual'),
                      ('S','Semi-auto')) 

engine_types       = (('D','Disel'),
                      ('P','Petrol'),
                      ('E','Electric'),
                      ('H','Hybrid'))

vehicle_types      = (('A','Automobile'),
                     ('M','Motorcycle'),
                     ('B','Bus'),
                     ('T','Truck'))

sell_status        =(('A','Active'),
                     ('S','Sold'),
                     ('P','Pending'),
                     ('D','Declined')


)
