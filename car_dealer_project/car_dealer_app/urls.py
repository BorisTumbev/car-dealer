from django.urls import path
from car_dealer_app import views


urlpatterns = [
    path('create',views.vehicle_create, name='create'),
    path('list',views.vehicle_list, name='list'),
    path('detail,<id>',views.vehicle_detail, name='detail')

]