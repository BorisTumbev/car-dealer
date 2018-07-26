from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .utils import *
from django.contrib.auth.models import User



class Make(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Model(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=15)
    make = models.ForeignKey(Make,on_delete = models.CASCADE)
    def __str__(self):
        return self.name
        
class Vehicle(models.Model):
    objects      = models.Manager()
    user         = models.ForeignKey(User,on_delete=models.PROTECT)

    make         = models.ForeignKey(Make,on_delete = models.CASCADE,null=True)
    model        = models.ForeignKey(Model,on_delete = models.CASCADE)
    v_type       = models.CharField(max_length=1,choices=vehicle_types)
    engine_type  = models.CharField(max_length=1,choices=engine_types)
    transmission = models.CharField(max_length=1,choices=transmission_types)
    condition    = models.CharField(max_length=1,choices=conditions)
    reg_number   = models.CharField(max_length=10,default='',unique=True)
    year         = models.PositiveIntegerField(validators=[MinValueValidator(1885),MaxValueValidator(curr_year)],null=True)
    price        = models.PositiveIntegerField(null=True)
    sold_for     = models.PositiveIntegerField(default=0)
    image        = models.ImageField(upload_to = 'images/',default='images/default_image.jpg')
    sell_status  = models.CharField(max_length=1,choices=sell_status,default="A")
    created_at   = models.DateTimeField(auto_now_add=True)
    description  = models.TextField(default='')

    def __str__(self):
        return self.reg_number