from django.urls import path
from . import views


urlpatterns = [

    path('create_user',     views.create_user,                      name='create_user'),
    path('edit_user/<id>',  views.edit_profile,{'self_prof':False}, name='edit_user'),
    path('edit_profile',    views.edit_profile,                     name='edit_profile'),
    path('delete_user/<id>',views.delete_user,                      name='delete_user'),

    path('users_list',      views.users_list,                       name='users_list'),

]