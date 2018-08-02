from .models import RentalVehicle, SellVehicle
from django.shortcuts import render
from .utils import pagination

def f_sell_veh_list(request):
    errorMsg="Empty Records"

    vehicles = SellVehicle.objects.filter(sell_status='A')

    return render(request,'./sell_veh_list_front.html',{'object_list':pagination(request,vehicles),"errorMsg":errorMsg})