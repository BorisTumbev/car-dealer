from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm,CustomUserChangeForm, CustomPasswordChangeForm
from django.contrib import messages
from .models import MyUser
from car_dealer_app.utils import pagination
from django.contrib.auth.decorators import login_required
from car_dealer_app.decorators import superuser_required
from django.contrib.auth import update_session_auth_hash


@superuser_required
def create_user(request):
    """
    view for creating user
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'user created')
            return redirect('users_list')
    else:
        form = CustomUserCreationForm()
    return render(request, './edit_user.html', {'form': form})


@superuser_required
def delete_user(request,id):
    """
    view for deleting objects
    """
    obj = get_object_or_404(MyUser,id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('home_back')
    return render(request, './delete.html', {'object':obj})

@login_required
def edit_profile(request,id=0,self_prof=True):
    
    """
    view for editing objects
    """
    if not self_prof and request.user.is_superuser:
        obj = get_object_or_404(MyUser,id=id)
    else:
        obj = request.user
    
    form = CustomUserChangeForm(request.POST or None,request.FILES or None, instance=obj,user=request.user)

    if form.is_valid():
        form.save()
        if self_prof:
            return redirect('home_back')
        else:
            return redirect('users_list')

    return render(request, './edit_user.html', {'form':form,'self_prof':self_prof})

@superuser_required
def users_list(request):

   
    object_list = MyUser.objects.all()
    
    return render(request,'./users_list.html',{'object_list':pagination(request,object_list)})


@login_required
def change_password(request):

    if request.method == 'POST':

        form = CustomPasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')

            return redirect('home_back')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, './change_pass.html', {'form': form})