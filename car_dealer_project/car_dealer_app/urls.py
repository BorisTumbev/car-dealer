from django.urls import path
from car_dealer_app import views 
from .forms import MakeForm, VehicleForm, CarModelForm
from .models import Vehicle, Make, Model


urlpatterns = [

    path('create_make',views.create_obj,{'i_form':MakeForm}, name='create_make'),
    path('create_model',views.create_obj,{'i_form':CarModelForm}, name='create_model'),
    path('create_vehicle',views.create_obj,{'i_form':VehicleForm}, name='create_vehicle'),

    path('vehicle_list',views.vehicle_list,{'all_vehicles':True}, name='vehicle_list'),
    path('my_list',views.vehicle_list, name='my_list'),
    path('sold_list',views.vehicle_list,{'all_sold':True}, name='sold_list'),

    path('detail/<id>',views.vehicle_detail, name='detail'),
    path('edit/<id>',views.vehicle_edit,{'i_form':VehicleForm,'model':Vehicle}, name='edit'),
    path('delete/<id>',views.vehicle_delete,{'model':Vehicle}, name='delete'),
    path('delete_make/<id>',views.vehicle_delete,{'model':Make}, name='delete_make'),

    path('create_user',views.create_user, name='create_user'),
    path('sell_vehicle/<id>',views.sell_vehicle, name='sell_vehicle')

]