from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import users_roles

class MyUser(AbstractUser):
      
    role  = models.CharField(max_length=15,choices=users_roles)
    image = models.ImageField(upload_to = 'images/users_app/',default='images/users_app/default_user_pic.jpg') 

    def __str__(self):
        return self.email
