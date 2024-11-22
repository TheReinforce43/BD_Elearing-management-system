from django.db import models 
from django.contrib.auth.models import AbstractUser, AbstractBaseUser 
from django.utils import timezone 
from User.custom_manager import CustomUserManager
from django.utils.translation import gettext_lazy as _



class User(AbstractBaseUser):
    email = models.EmailField(_('Email address'),unique=True)
    phone_number = models.CharField(_('Phone number'),max_length=20,null=True)
    full_name = models.CharField(_('Full name'),max_length=100,null=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=[]

    objects = CustomUserManager()


    def __str__(self) -> str:
        return self.email 










    



