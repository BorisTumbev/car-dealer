from django.urls import path
from car_dealer_app import views, front_office_views, utils 
from .forms import *
from .models import RentalVehicle, SellVehicle , MyUser
from django.views.generic.base import TemplateView

urlpatterns = [

    
    #urls for creating objects
    
    path('create_make',     views.create_obj,   {'i_form':MakeForm},            name='create_make'),
    path('create_model',    views.create_obj,   {'i_form':CarModelForm},        name='create_model'),
    path('create_rental',   views.create_obj,   {'i_form':RentalVehicleForm},   name='create_rental'),
    path('create_sell',     views.create_obj,   {'i_form':SellVehicleForm},     name='create_sell'),
    path('create_message',  views.create_obj,   {'i_form':MessageForm},         name='create_message'),

    path('create_user',     views.create_user,                                  name='create_user'),

    #urls for listing objects

    path('rented_list',     views.rental_veh_list,                              name='rented_list'),
    path('rental_list',     views.rental_veh_list,{'rented':False},             name='rental_list'),
    path('users_list',      views.user_list,                                    name='users_list'),
    path('list_message',    views.list_message,                                 name='list_message'),
    path('sell_list',       views.sell_veh_list,{'all_vehicles':True},          name='sell_list'),
    path('sold_list',       views.sell_veh_list,{'status':'S'},                 name='sold_list'),
    path('pending_list',    views.sell_veh_list,{'status':'P'},                 name='pending_list'),
    path('log_list',        views.log_list,                                     name='log_list'),


    #urls for editing objects

    path('edit_rental/<id>',views.edit_obj,     {'i_form':RentalVehicleForm,'model':RentalVehicle}, name='edit_rental'),
    path('edit_sell/<id>',  views.edit_obj,     {'i_form':SellVehicleForm,'model':SellVehicle},     name='edit_sell'),
    path('edit_user/<id>',  views.edit_obj,     {'i_form':CustomUserChangeForm,'model':MyUser},     name='edit_user'),


    #urls for deleting objects
    
    path('delete_rental/<id>',views.delete_obj, {'model':RentalVehicle},        name='delete_rental'),
    path('delete_sell/<id>',  views.delete_obj, {'model':SellVehicle},          name='delete_sell'),
    path('delete_user/<id>',  views.delete_obj, {'model':MyUser},               name='delete_user'),
    path('delete_old_logs',   views.del_old_logs,                               name='delete_old_logs'),

    #urls for object deatails

    path('detail_rental/<id>',views.veh_detail, {'car_type':RentalVehicle},     name='detail_rental'),
    path('detail_sell/<id>',  views.veh_detail, {'car_type':SellVehicle},       name='detail_sell'),

    #-----

    path('rent_veh/<id>',        views.rent_veh,                                 name='rent_veh'),
    path('return_veh/<id>',      views.rent_veh,    {'rent':False},              name='return_veh'),
    path('sell_vehicle/<id>',    views.sell_vehicle,                             name='sell_vehicle'),
    path('retrieve_vehicle/<id>',views.sell_vehicle,{'sell':False},              name='retrieve_vehicle'),


    #template views

    path('home',                 views.home,                                    name='home_back'),
    path('',    TemplateView.as_view(template_name='home_front_office.html'),   name='home_front'),

    #front office views

    path('f_rental_list',front_office_views.f_rent_veh_list,                    name='f_rental_list'),
    path('f_sell_list',  front_office_views.f_sell_veh_list,                    name='f_sell_list')
    
    # path('order_price',views.obj_order,{'order':'price'},name='order_price'),
    # path('order_type',views.obj_order,{'order':'v_type'},name='order_type'),
    # path('rent/<id>',views.rent_obj, name='rent'),
]

