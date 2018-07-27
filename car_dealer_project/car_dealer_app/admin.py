from django.contrib import admin
from .models import Vehicle, Make, Model

admin.site.register(Vehicle)
admin.site.register(Make)
admin.site.register(Model)