from django.db import models
from django.core.validators import MaxValueValidator
import datetime
from .choices import *


curr_year = datetime.datetime.now().year

class Vehicle(models.Model):
    objects      = models.Manager()

    brand        = models.CharField(max_length=15)
    model        = models.CharField(max_length=15)
    v_type       = models.CharField(max_length=2,choices=vehicle_types)
    engine_type  = models.CharField(max_length=1,choices=engine_types)
    transmission = models.CharField(max_length=1,choices=transmission_types)
    condition    = models.CharField(max_length=1,choices=conditions)
    reg_number   = models.CharField(max_length=10,default='',unique=True)
    year         = models.PositiveIntegerField(validators=[MaxValueValidator(curr_year)],null=True)
    price        = models.PositiveIntegerField(null=True)

    #image        = models.ImageField(upload_to = 'images/')
    sold         = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    description  = models.TextField(default='')