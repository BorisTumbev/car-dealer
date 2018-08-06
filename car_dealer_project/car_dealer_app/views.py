from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from .models import RentalVehicle, Make, Model, SellVehicle , MyUser,Log,Message
from .decorators import *
from .utils import pagination, mail_send
from .forms import RentalVehicleForm,SellVehicleForm,CustomUserCreationForm,RentForm,CustomUserChangeForm
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime
from datetime import timedelta


@login_required
def create_obj(request,i_form):
    """
    view for creating objects
    """
   
    form = i_form(request.POST or None,request.FILES or None,user=request.user)

    if form.is_valid():
        
        form.save()
        create_log(request,i_form.__name__[:-4],'created',request.user)

        return redirect('home_back')

    return render(request, './create.html', {'form':form})


@superuser_required
def edit_obj(request,id,i_form,model):
    
    """
    view for editing objects
    """
    obj = get_object_or_404(model,id=id)

    if i_form == CustomUserChangeForm:
        form = i_form(request.POST or None,request.FILES or None, instance=obj)
    else:
        form = i_form(request.POST or None,request.FILES or None, instance=obj,user=request.user)

    if form.is_valid():
        form.save()
        create_log(request,i_form.__name__[:-4],'edited',request.user)
        return redirect('home_back')

    return render(request, './create.html', {'form':form})


@superuser_required
def delete_obj(request,id,model):
    """
    view for deleting objects
    """
    obj = get_object_or_404(model,id=id)
    if request.method=='POST':
        obj.delete()
        create_log(request,model.__name__,'deleted',request.user)
        return redirect('home_back')
    return render(request, './delete.html', {'object':obj})


@login_required
def veh_detail(request,id,car_type):
    """
    view for showing all information for a vehicle
    """
    vehicle = get_object_or_404(car_type,id=id)

    return render(request,'./detail.html',{'object':vehicle})


@sales_user_required
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
    
    # if status=="A":
    #     vehicles = SellVehicle.objects.filter(Q(sell_status="A")|Q(sell_status="P"),user=request.user)

    if status=="S":
        vehicles = SellVehicle.objects.filter(sell_status="S")
            
    if status=="P":
        vehicles = SellVehicle.objects.filter(sell_status="P")
        
    if all_vehicles:
        vehicles = SellVehicle.objects.filter(Q(sell_status="A")|Q(sell_status="P"))

    return render(request,'./sell_veh_list.html',{'object_list':pagination(request,vehicles),"errorMsg":errorMsg})
    
@rental_user_required
def rental_veh_list(request,rented=True):
    errorMsg="Empty Records"
    
    form = RentForm(request.POST or None,request.FILES or None,user=request.user)

    query = request.GET.get('q')
    if query:
        vehicles = RentalVehicle.objects.filter(
                                        Q(reg_number__icontains=query) |
                                        Q(make__name__icontains=query) |
                                        Q(model__name__icontains=query)|
                                        Q(v_type__icontains=query)
                                        ).distinct()
                                        
        return render(request,'./rental_veh_list.html',{'object_list':pagination(request,vehicles),"errorMsg":errorMsg})

    if rented:
        vehicles = RentalVehicle.objects.filter(rental_status=True)
    else:
        vehicles = RentalVehicle.objects.filter(rental_status=False)

    return render(request,'./rental_veh_list.html',{'object_list':pagination(request,vehicles),"errorMsg":errorMsg,'form':form})



@sales_user_required
def sell_vehicle(request,id,sell=True):
    """
    view that changes sell_status of a Vehicle object
    """
    obj = get_object_or_404(SellVehicle,id=id)

    if request.user.is_superuser:
        if not sell:
            obj.sell_status="A"
            obj.save()
            return redirect('sell_list')
        else:
            obj.sell_status= "S"
            obj.save()
            create_log(request,'Vehicle','vehicle sold',request.user)  
            messages.success(request, 'Vehicle Sold')     
            return redirect('sold_list')
    else:
        obj.sell_status = "P"
        obj.save()
        mail_send(("{} wants to sell {} {} {} ").format(request.user.username,obj.reg_number,obj.make.name,obj.model.name))
       
        messages.success(request, 'Request for selling sent')
        return redirect('sell_list')


@rental_user_required
def rent_veh(request,id,rent=True):
    
    """
    view for renting vehicle
    """
    obj = get_object_or_404(RentalVehicle,id=id)

    if not rent:
        obj.rental_status = False
        obj.rented_until = None
        obj.rented_at = None
        obj.save()
        return redirect('rental_list')

    form = RentForm(request.POST or None,request.FILES or None, instance=obj,user=request.user)

    if form.is_valid():
        obj.rental_status = True
        obj.rented_at = datetime.datetime.now()
        form.save()
        create_log(request,'Vehicle','vehicle rented',request.user)
        return redirect('rented_list')

    #return render(request, './create.html', {'form':form})


@superuser_required
def create_user(request):
    """
    view for creating user
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            create_log(request,"User",'created user',request.user)
            messages.success(request, 'user created')
            return redirect('home_back')
    else:
        form = CustomUserCreationForm()
    return render(request, './create.html', {'form': form})


@superuser_required
def user_list(request):

    object_list = MyUser.objects.all()

    return render(request,'./users_list.html',{'object_list':pagination(request,object_list)})
    
    

@login_required
def list_models(request,model_type):
    """
    view for listing models and makes
    """
    query = request.GET.get('q')

    if query:
        object_list = model_type.objects.filter(name__icontains=query)
    else:
        object_list = model_type.objects.all()

    if model_type==Model:
        return render(request,'./list_models.html',{'object_list':pagination(request,object_list)})
    else:
        return render(request,'./list_makes.html',{'object_list':pagination(request,object_list)})


def create_log(request,obj,action,user,date=datetime.datetime.now()):
    
    log = Log(user=user,action=action,object_type=obj,date=date)

    log.save()
    
@superuser_required
def log_list(request):

    object_list = Log.objects.all()

    return render(request,'./log_list.html',{'object_list':pagination(request,object_list)})


@superuser_required
def del_old_logs(request):

    object_list = Log.objects.filter(date__lt=(datetime.datetime.now()-timedelta(weeks=8)))

    if request.method=='POST':
        object_list.delete() 
        return redirect('log_list')
    return render(request, './delete.html', {'object':object_list})

def list_message(request):
    obj_list = Message.objects.all()

    return render(request,'./base_back_office.html',{'obj_list':obj_list})



def error_404(request):
    return render(request, './errors/404.html')




# def obj_order(request,order):
#     """
#     view that orders vehicle object by price and type
#     """

#     vehicles = Vehicle.objects.order_by('-'+order)

#     return render(request,'./list_vehicle.html',{'object_list':pagination(request,vehicles)})