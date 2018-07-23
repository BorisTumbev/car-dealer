from django.shortcuts import render, redirect, get_object_or_404
from .forms import VehicleForm
from .models import Vehicle



def vehicle_create(request):
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('')

    return render(request, './create.html', {'form':form})

def vehicle_list(request):
    vehicles = Vehicle.objects.all()

    return render(request,'./list.html',{'object_list':vehicles})

def vehicle_detail(request,id):
    vehicle = get_object_or_404(Vehicle,id=id)

    return render(request,'./detail.html',{'object':vehicle})