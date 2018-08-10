from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.shortcuts import render


def error_404(request,exception):
    return render(request, './errors/404.html')


def pagination(request,object_list):
    """
    function for making pages
    """

    paginator = Paginator(object_list, 10)

    page = request.GET.get('page')
    limited_obj = paginator.get_page(page)
    return limited_obj

def mail_send(msg):
    """
    func for shorting send mail
    """
    send_mail(subject='Selling request',message=msg,from_email='test.mycode9999@gmail.com',recipient_list=['test.mycode9999@gmail.com'],fail_silently=False,)


"""
field choices for the models
"""

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
