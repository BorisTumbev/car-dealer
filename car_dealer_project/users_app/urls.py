from django.urls import path
from . import views
import django.contrib.auth.urls
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetFrom





urlpatterns = [

    path('create_user',     views.create_user,                      name='create_user'),
    path('edit_user/<id>',  views.edit_profile,{'self_prof':False}, name='edit_user'),
    path('edit_profile',    views.edit_profile,                     name='edit_profile'),
    path('delete_user/<id>',views.delete_user,                      name='delete_user'),

    path('users_list',      views.users_list,                       name='users_list'),

    path('change_pass',     views.change_password,                  name = 'change_pass'),

    path('password_reset', auth_views.PasswordResetView.as_view(form_class=CustomPasswordResetFrom), name='pass_reset'),
]

