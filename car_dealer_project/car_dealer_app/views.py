from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from .models import RentalVehicle, Make, Model, SellVehicle
from .decorators import superuser_required
from .utils import pagination
from .forms import RentalVehicleForm


@login_required
def create_obj(request,i_form):
    """
    view for creating objects
    """
   
    form = i_form(request.POST or None,request.FILES or None,user=request.user)

    if form.is_valid():
        
        form.save()
        return redirect('/')

    return render(request, './create.html', {'form':form})




@login_required
def sell_veh_list(request,status='N',all_vehicles=False):
    """
    view for listing and sorting vehiclesS
    """

    errorMsg="Empty Records"

    query = request.GET.get('q')
    if query:
        vehicles = SellVehicle.objects.filter(
                                        Q(reg_number__icontains=query) |
                                        Q(make__name__icontains=query) |
                                        Q(model__name__icontains=query)|
                                        Q(v_type__icontains=query)
                                        ).distinct()
                                        
        return render(request,'./sell_veh_list.html',{'object_list':pagination(request,vehicles),"errorMsg":errorMsg})
    
    if status=="A":
        vehicles = SellVehicle.objects.filter(Q(sell_status="A")|Q(sell_status="P"),user=request.user)

    if status=="S":
        vehicles = SellVehicle.objects.filter(sell_status="S")
            
    if status=="P":
        vehicles = SellVehicle.objects.filter(sell_status="P")
        
    if all_vehicles:
        vehicles = SellVehicle.objects.filter(Q(sell_status="A")|Q(sell_status="P"))

    return render(request,'./sell_veh_list.html',{'object_list':pagination(request,vehicles),"errorMsg":errorMsg})
    
def rental_veh_list(request):
    errorMsg="Empty Records"


    query = request.GET.get('q')
    if query:
        vehicles = RentalVehicle.objects.filter(
                                        Q(reg_number__icontains=query) |
                                        Q(make__name__icontains=query) |
                                        Q(model__name__icontains=query)|
                                        Q(v_type__icontains=query)
                                        ).distinct()
                                        
        return render(request,'./rental_veh_list.html',{'object_list':pagination(request,vehicles),"errorMsg":errorMsg})
    vehicles = RentalVehicle.objects.all()
    return render(request,'./rental_veh_list.html',{'object_list':pagination(request,vehicles),"errorMsg":errorMsg})


@login_required
def vehicle_detail(request,id):
    """
    view for showing all information for a vehicle
    """
    vehicle = get_object_or_404(SellVehicle,id=id)

    return render(request,'./detail.html',{'object':vehicle})

@superuser_required
def edit_obj(request,id,i_form,model):
    
    """
    view for editing objects
    """
    obj = get_object_or_404(model,id=id)

    form = i_form(request.POST or None,request.FILES or None, instance=obj,user=request.user)

    if form.is_valid():
        form.save()
        return redirect('vehicle_list')

    return render(request, './create.html', {'form':form})


@superuser_required
def delete_obj(request,id,model):
    """
    view for deleting objects
    """
    obj = get_object_or_404(model,id=id)
    if request.method=='POST':
        obj.delete()
        
        return redirect('vehicle_list')
    return render(request, './delete.html', {'object':obj})


@superuser_required
def create_user(request):
    """
    view for creating user
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'user created')
            return redirect('vehicle_list')
    else:
        form = UserCreationForm()
    return render(request, './registration/create_user.html', {'form': form})


@login_required
def sell_vehicle(request,id,sell=True):
    """
    view that changes sell_status of a Vehicle object
    """
    obj = get_object_or_404(SellVehicle,id=id)

    if request.user.is_superuser:
        if not sell:
            obj.sell_status="A"
            obj.save()
            return redirect('vehicle_list')
        else:
            obj.sell_status= "S"
            obj.save()  
            messages.success(request, 'Vehicle Sold')     
            return redirect('sold_list')
    else:
        obj.sell_status = "P"
        obj.save()
        send_mail('Selling request',request.user.username+" wants to sell "+obj.reg_number+" "+obj.make.name+" "+obj.model.name,'test.mycode9999@gmail.com',['test.mycode9999@gmail.com'],fail_silently=False,)
        messages.success(request, 'Request for selling sent')
        return redirect('my_list')
    
    

@login_required
def list_models(request,model):
    """
    view for listing models and makes
    """
    query = request.GET.get('q')

    if query:
        object_list = model.objects.filter(name__icontains=query)
    else:
        object_list = model.objects.all()

    if model==Model:
        return render(request,'./list_models.html',{'object_list':pagination(request,object_list)})
    else:
        return render(request,'./list_makes.html',{'object_list':pagination(request,object_list)})

# def obj_order(request,order):
#     """
#     view that orders vehicle object by price and type
#     """

#     vehicles = Vehicle.objects.order_by('-'+order)

#     return render(request,'./list_vehicle.html',{'object_list':pagination(request,vehicles)})

def rent_veh(request,id,rent=True):

    obj = get_object_or_404(RentalVehicle,id=id)
    if rent:
        obj.rental_status = True
    else:
        obj.rental_status = False
        
    obj.save()

    return redirect('rental_list')