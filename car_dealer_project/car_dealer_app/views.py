from django.shortcuts import render, redirect, get_object_or_404
from .forms import VehicleForm
from .models import Vehicle, Make, Model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import superuser_required
from django.db.models import Q


@login_required
def create_obj(request,i_form):
    
    # if not Make.objects.all():
    #     return render(request, './create.html', {'errorMsg':'Create Make and Model first'})

    form = i_form(request.POST or None,request.FILES or None,user=request.user)

    if form.is_valid():
        form.save()
        return redirect('vehicle_list')

    return render(request, './create.html', {'form':form})





@login_required
def vehicle_list(request,status="A",all_vehicles=False):

    query = request.GET.get('q')
    if query:
        vehicles = Vehicle.objects.filter(
                                        Q(reg_number__icontains=query) |
                                        Q(make__name__icontains=query) |
                                        Q(model__name__icontains=query)
                                        ).distinct()
                                        
        return render(request,'./list.html',{'object_list':vehicles})

    if status=="S":
        vehicles = Vehicle.objects.filter(sell_status="S")
        return render(request,'./list.html',{'object_list':vehicles})

    if status=="P":
        vehicles = Vehicle.objects.filter(sell_status="P")
        return render(request,'./list.html',{'object_list':vehicles})

    if all_vehicles:
        vehicles = Vehicle.objects.filter(Q(sell_status="A")|Q(sell_status="P"))
        return render(request,'./list.html',{'object_list':vehicles})



    vehicles = Vehicle.objects.filter(Q(sell_status="A")|Q(sell_status="P"),user=request.user)



    return render(request,'./list.html',{'object_list':vehicles})




@login_required
def vehicle_detail(request,id):
    vehicle = get_object_or_404(Vehicle,id=id)

    return render(request,'./detail.html',{'object':vehicle})

@login_required
def edit_obj(request,id,i_form,model):

    if model==Make or model==Model:
        obj = get_object_or_404(model,id=id)
    else:  
        obj = get_object_or_404(model,id=id,user=request.user)

    form = i_form(request.POST or None,request.FILES or None, instance=obj,user=request.user)

    if form.is_valid():
        form.save()
        return redirect('vehicle_list')

    return render(request, './create.html', {'form':form})


@superuser_required
def delete_obj(request,id,model):
    obj = get_object_or_404(model,id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('vehicle_list')
    return render(request, './delete.html', {'object':obj})


@superuser_required
def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = UserCreationForm()
    return render(request, './create_user.html', {'form': form})


@login_required
def sell_vehicle(request,id):
    obj = get_object_or_404(Vehicle,id=id)
    if request.user.is_superuser:
        obj.sell_status= "S"
        obj.save()
       
    else:
        obj.sell_status = "P"
        obj.save()

    return redirect('vehicle_list')



def list_models(request,model):
    query = request.GET.get('q')
    if query:
        object_list = model.objects.filter(name__icontains=query)
        dic = {'object_list':object_list}                       
        if model==Model:
            return render(request,'./list_models.html',dic)
        else:
            return render(request,'./list_makes.html',dic)

    object_list = model.objects.all()

    if model==Model:
        return render(request,'./list_models.html',{'object_list':object_list})
    else:
        return render(request,'./list_makes.html',{'object_list':object_list})