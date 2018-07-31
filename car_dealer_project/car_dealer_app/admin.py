from django.contrib import admin
from .models import RentalVehicle, Make, Model, SellVehicle

admin.site.register(SellVehicle)
admin.site.register(RentalVehicle)
admin.site.register(Make)
admin.site.register(Model)