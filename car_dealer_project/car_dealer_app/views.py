from django.shortcuts import render, redirect, get_object_or_404
from .forms import VehicleForm
from .models import Vehicle, Make, Model



def vehicle_create(request):
    if not Make.objects.all():
        return render(request, './create.html', {'errorMsg':'Create Make first'})

    form = VehicleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, './create.html', {'form':form})

def vehicle_list(request):
    vehicles = Vehicle.objects.all()

    return render(request,'./list.html',{'object_list':vehicles})

def vehicle_detail(request,id):
    vehicle = get_object_or_404(Vehicle,id=id)

    return render(request,'./detail.html',{'object':vehicle})

def vehicle_edit(request,id):
    vehicle = get_object_or_404(Vehicle,id=id)
    form = VehicleForm(request.POST or None, instance=vehicle)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, './create.html', {'form':form})

def vehicle_delete(request,id):
    vehicle = get_object_or_404(Vehicle,id=id)
    if request.method=='POST':
        vehicle.delete()
        return redirect('list')
    return render(request, './delete.html', {'object':vehicle})
