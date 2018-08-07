from .models import RentalVehicle, SellVehicle
from django.shortcuts import render
from .utils import pagination
from django.db.models import Q


def f_rent_veh_list(request):
    """
    list of all available rental vehicles
    """
    errorMsg="Empty Records"

    query = request.GET.get('q')
    if query:
        vehicles = RentalVehicle.objects.filter(
                                        Q(rental_status = False) &(
                                        Q(make__name__icontains=query) |
                                        Q(model__name__icontains=query)|
                                        Q(v_type__icontains=query))
                                        ).distinct()
                                        
        return render(request,'./veh_list_front.html',{'object_list':pagination(request,vehicles),"errorMsg":errorMsg})

    vehicles = RentalVehicle.objects.filter(rental_status=False)
   
    return render(request,'./veh_list_front.html',{'object_list':pagination(request,vehicles),"errorMsg":errorMsg})


def f_sell_veh_list(request):
    """
    list of all available for sale vehicles
    """

    errorMsg="Empty Records"

    query = request.GET.get('q')
    if query:
        vehicles = SellVehicle.objects.filter(
                                        Q(sell_status = 'A') &(
                                        Q(make__name__icontains=query) |
                                        Q(model__name__icontains=query)|
                                        Q(v_type__icontains=query))
                                        ).distinct()
                                        
        return render(request,'./veh_list_front.html',{'object_list':pagination(request,vehicles),"errorMsg":errorMsg})

    vehicles = SellVehicle.objects.filter(sell_status='A')
   
    return render(request,'./veh_list_front.html',{'object_list':pagination(request,vehicles),"errorMsg":errorMsg})