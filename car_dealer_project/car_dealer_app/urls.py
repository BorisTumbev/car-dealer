from django.urls import path
from car_dealer_app import views


urlpatterns = [
    path('create',views.vehicle_create, name='create'),
    path('list',views.vehicle_list, name='list'),
    path('detail,<id>',views.vehicle_detail, name='detail'),
    path('edit,<id>',views.vehicle_edit, name='edit'),
    path('delete,<id>',views.vehicle_delete, name='delete')

]