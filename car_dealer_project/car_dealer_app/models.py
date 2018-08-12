from django.db import models
from .utils import vehicle_types, engine_types,transmission_types,conditions,sell_status
import datetime
from .validators import *
from users_app.models import MyUser

class Make(models.Model):
    objects = models.Manager()

    name    = models.CharField(max_length=15,unique=True)

    def __str__(self):
        return self.name

class Model(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=15,unique=True)
    make = models.ForeignKey(Make,on_delete = models.CASCADE)

    def __str__(self):
        return self.name
        
class Vehicle(models.Model):

    objects      = models.Manager()

    user         = models.ForeignKey(MyUser,on_delete=models.PROTECT)
    make         = models.ForeignKey(Make,on_delete = models.PROTECT,null=True)
    model        = models.ForeignKey(Model,on_delete = models.PROTECT)
    v_type       = models.CharField(max_length=1,choices=vehicle_types)
    engine_type  = models.CharField(max_length=1,choices=engine_types)
    transmission = models.CharField(max_length=1,choices=transmission_types)
    condition    = models.CharField(max_length=1,choices=conditions)
    reg_number   = models.CharField(max_length=10,default='',unique=True)
    year         = models.PositiveIntegerField(validators=[curr_year_validator],null=True)
    image        = models.ImageField(upload_to = 'images/car_dealer_app/',default='images/car_dealer_app/default_image.jpg')
    created_at   = models.DateTimeField(auto_now_add=True)
    description  = models.TextField(default='')

    class Meta:
        abstract = True


class RentalVehicle(Vehicle):

    rental_price_per_day  = models.PositiveIntegerField()
    rental_status         = models.BooleanField(default=False)
    rented_at             = models.DateTimeField(default=None,null=True)
    rented_until          = models.DateTimeField(default=None,null=True,validators=[curr_day_validator])

   
    def __str__(self):
        return self.reg_number
    
class SellVehicle(Vehicle):
    
    price       = models.PositiveIntegerField(null=True)
    sell_status = models.CharField(max_length=1,choices=sell_status,default="A")

    def __str__(self):
        return self.reg_number

class Log(models.Model):
    objects      = models.Manager()

    user         = models.ForeignKey(MyUser,on_delete=models.PROTECT)
    action       = models.CharField(max_length=50)
    object_type  = models.CharField(max_length=50)
    date         = models.DateTimeField()


class Message(models.Model):
    objects      = models.Manager()

    description = models.TextField()
    date_added  = models.DateTimeField(auto_now_add=True)
    user        = models.ForeignKey(MyUser,on_delete = models.PROTECT)
