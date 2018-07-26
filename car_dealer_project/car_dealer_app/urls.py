from django.urls import path
from car_dealer_app import views 
from .forms import MakeForm, VehicleForm, CarModelForm
from .models import Vehicle, Make, Model


urlpatterns = [

    
    #urls for creating objects
    
    path('create_make',views.create_obj,{'i_form':MakeForm}, name='create_make'),
    path('create_model',views.create_obj,{'i_form':CarModelForm}, name='create_model'),
    path('create_vehicle',views.create_obj,{'i_form':VehicleForm}, name='create_vehicle'),

    #urls for listing objects

    path('vehicle_list',views.vehicle_list,{'all_vehicles':True}, name='vehicle_list'),
    path('my_list',views.vehicle_list,{'status':'A'}, name='my_list'),
    path('sold_list',views.vehicle_list,{'status':'S'}, name='sold_list'),
    path('pending_list',views.vehicle_list,{'status':'P'}, name='pending_list'),

    path('model_list',views.list_models,{'model':Model}, name='model_list'),
    path('make_list',views.list_models,{'model':Make}, name='make_list'),


    #urls for editing objects

    path('edit/<id>',views.edit_obj,{'i_form':VehicleForm,'model':Vehicle}, name='edit'),
    path('edit_make/<id>',views.edit_obj,{'i_form':MakeForm,'model':Make}, name='edit_make'),
    path('edit_model/<id>',views.edit_obj,{'i_form':CarModelForm,'model':Model}, name='edit_model'),


    #urls for deleting objects
    
    path('delete/<id>',views.delete_obj,{'model':Vehicle}, name='delete'),
    path('delete_make/<id>',views.delete_obj,{'model':Make}, name='delete_make'),
    path('delete_model/<id>',views.delete_obj,{'model':Model}, name='delete_model'),


    path('detail/<id>',views.vehicle_detail, name='detail'),

    path('order_price',views.obj_order,{'order':'price'},name='order_price'),
    path('order_type',views.obj_order,{'order':'v_type'},name='order_type'),

    path('create_user',views.create_user, name='create_user'),

    path('sell_vehicle/<id>',views.sell_vehicle, name='sell_vehicle'),
    path('retrieve_vehicle/<id>',views.sell_vehicle,{'sell':False}, name='retrieve_vehicle')

]