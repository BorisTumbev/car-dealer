from django.urls import path
from car_dealer_app import views, front_office_views 
from .forms import MakeForm, RentalVehicleForm, CarModelForm, SellVehicleForm, CustomUserCreationForm
from .models import RentalVehicle, Make, Model, SellVehicle , MyUser
from django.conf.urls import handler404

urlpatterns = [

    
    #urls for creating objects
    
    path('create_make',views.create_obj,{'i_form':MakeForm}, name='create_make'),
    path('create_model',views.create_obj,{'i_form':CarModelForm}, name='create_model'),
    path('create_rental',views.create_obj,{'i_form':RentalVehicleForm}, name='create_rental'),
    path('create_sell',views.create_obj,{'i_form':SellVehicleForm}, name='create_sell'),

    #urls for listing objects

    path('rented_list',views.rental_veh_list, name='rented_list'),
    path('rental_list',views.rental_veh_list,{'rented':False}, name='rental_list'),

    path('users_list',views.user_list, name='users_list'),
   
    path('sell_list',views.sell_veh_list,{'all_vehicles':True}, name='sell_list'),
    #path('my_list',views.sell_veh_list,{'status':'A'}, name='my_list'),
    path('sold_list',views.sell_veh_list,{'status':'S'}, name='sold_list'),
    path('pending_list',views.sell_veh_list,{'status':'P'}, name='pending_list'),

    path('model_list',views.list_models,{'model_type':Model}, name='model_list'),
    path('make_list',views.list_models,{'model_type':Make}, name='make_list'),

    path('log_list',views.log_list, name='log_list'),

    path('',front_office_views.f_sell_veh_list, name='f_sell_list'),
    path('f_rental_list',front_office_views.f_rent_veh_list, name='f_rental_list'),


    #urls for editing objects

    path('edit_rental/<id>',views.edit_obj,{'i_form':RentalVehicleForm,'model':RentalVehicle}, name='edit_rental'),
    path('edit_sell/<id>',views.edit_obj,{'i_form':SellVehicleForm,'model':SellVehicle}, name='edit_sell'),
    path('edit_make/<id>',views.edit_obj,{'i_form':MakeForm,'model':Make}, name='edit_make'),
    path('edit_model/<id>',views.edit_obj,{'i_form':CarModelForm,'model':Model}, name='edit_model'),
    path('edit_user/<id>',views.edit_obj,{'i_form':CustomUserCreationForm,'model':MyUser}, name='edit_user'),



    #urls for deleting objects
    
    path('delete_rental/<id>',views.delete_obj,{'model':RentalVehicle}, name='delete_rental'),
    path('delete_sell/<id>',views.delete_obj,{'model':SellVehicle}, name='delete_sell'),
    path('delete_make/<id>',views.delete_obj,{'model':Make}, name='delete_make'),
    path('delete_model/<id>',views.delete_obj,{'model':Model}, name='delete_model'),
    path('delete_user/<id>',views.delete_obj,{'model':MyUser}, name='delete_user'),

    path('delete_old_logs',views.del_old_logs, name='delete_old_logs'),


    path('detail_rental/<id>',views.veh_detail,{'car_type':RentalVehicle}, name='detail_rental'),
    path('detail_sell/<id>',views.veh_detail,{'car_type':SellVehicle}, name='detail_sell'),

    # path('order_price',views.obj_order,{'order':'price'},name='order_price'),
    # path('order_type',views.obj_order,{'order':'v_type'},name='order_type'),
    path('rent_veh/<id>',views.rent_veh, name='rent_veh'),
    path('return_veh/<id>',views.rent_veh,{'rent':False}, name='return_veh'),
    
   # path('rent/<id>',views.rent_obj, name='rent'),


    path('create_user',views.create_user, name='create_user'),

    path('sell_vehicle/<id>',views.sell_vehicle, name='sell_vehicle'),
    path('retrieve_vehicle/<id>',views.sell_vehicle,{'sell':False}, name='retrieve_vehicle')

]

handler404 = views.error_404
