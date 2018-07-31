from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .utils import *
from django.contrib.auth.models import User
import datetime


class Make(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=15,unique=True)
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
    user         = models.ForeignKey(User,on_delete=models.PROTECT)

    make         = models.ForeignKey(Make,on_delete = models.PROTECT,null=True)
    model        = models.ForeignKey(Model,on_delete = models.PROTECT)
    v_type       = models.CharField(max_length=1,choices=vehicle_types)
    engine_type  = models.CharField(max_length=1,choices=engine_types)
    transmission = models.CharField(max_length=1,choices=transmission_types)
    condition    = models.CharField(max_length=1,choices=conditions)
    reg_number   = models.CharField(max_length=10,default='',unique=True)
    year         = models.PositiveIntegerField(validators=[curr_year_validator],null=True)
    image        = models.ImageField(upload_to = 'images/',default='images/default_image.jpg')
    created_at   = models.DateTimeField(auto_now_add=True)
    description  = models.TextField(default='')

    class Meta:
        abstract = True


class RentalVehicle(Vehicle):
    rental_price_per_day  = models.PositiveIntegerField()
    rental_status         = models.BooleanField(default=False)
    rented_at             = models.DateTimeField(default=None,null=True)

    def save(self,*args,**kwargs):
        if self.rental_status:
            self.rented_at = datetime.datetime.now()
        else:
            self.rented_at = None

        super().save(*args,**kwargs)
   
    def __str__(self):
        return self.reg_number
    
class SellVehicle(Vehicle):
    price       = models.PositiveIntegerField(null=True)
    sell_status = models.CharField(max_length=1,choices=sell_status,default="A")

    def __str__(self):
        return self.reg_number