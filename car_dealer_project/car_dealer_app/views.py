from django.shortcuts import render, redirect, get_object_or_404
from .forms import VehicleForm
from .models import Vehicle, Make, Model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import superuser_required
from django.db.models import Q


@login_required
def create_obj(request,i_form):
    if not Make.objects.all() and not Model.objects.all():
        return render(request, './create.html', {'errorMsg':'Create Make and Model first'})

    form = i_form(request.POST or None,request.FILES or None,user=request.user)
    if form.is_valid():
        form.save()
        return redirect('vehicle_list')

    return render(request, './create.html', {'form':form})

@login_required
def vehicle_list(request,all_vehicles=False,all_sold=False):

    query = request.GET.get('q')
    if query:
        vehicles = Vehicle.objects.filter(
                                        Q(reg_number__icontains=query) |
                                        Q(make__name__icontains=query) |
                                        Q(model__name__icontains=query)
                                        ).distinct()
                                        
        return render(request,'./list.html',{'object_list':vehicles})

    if all_sold:
        vehicles = Vehicle.objects.filter(sold=True)
        return render(request,'./list.html',{'object_list':vehicles})


    if all_vehicles:
        vehicles = Vehicle.objects.filter(sold=False)
        return render(request,'./list.html',{'object_list':vehicles})

    vehicles = Vehicle.objects.filter(sold=False,user=request.user)



    return render(request,'./list.html',{'object_list':vehicles})




@login_required
def vehicle_detail(request,id):
    vehicle = get_object_or_404(Vehicle,id=id)

    return render(request,'./detail.html',{'object':vehicle})

@login_required
def vehicle_edit(request,id,i_form,model):

    obj = get_object_or_404(model,id=id,user=request.user)
  

    form = i_form(request.POST or None,request.FILES or None, instance=obj,user=request.user)

    if form.is_valid():
        form.save()
        return redirect('vehicle_list')

    return render(request, './create.html', {'form':form})


@superuser_required
def vehicle_delete(request,id,model):
    obj = get_object_or_404(model,id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('vehicle_list')
    return render(request, './delete.html', {'object':obj})


# def serach(request):
    
#     if request.method == 'GET':

#         search_query = request.GET.get('search_box', None)


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
    obj.sold= True
    obj.save()
    return redirect('vehicle_list')

# def calc(request):

#     if request.method == 'POST':
#         form = SellForm(request.POST)

#         if form.is_valid():
#             field1 = form.cleaned_data.get('field1')
            
#             return render(request,'../templates/answ.html', {'answ': field1})
#             #return HttpResponseRedirect('/index')
#     else:
#         form = SellForm()

#     return render(request,'../templates/calc.html', {'form': form})