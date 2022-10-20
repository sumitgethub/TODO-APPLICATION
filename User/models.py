from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self,username,password = None,password2=None,**extra_fields):
        if not username:
            raise ValueError('username must be provided')

        user = self.model(
            
            username = username,
            **extra_fields
            )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username,password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        return self.create_user(username,password,**extra_fields)


#user model
class User(AbstractUser):
    username = models.CharField(max_length=12,unique=True,blank=True,null=True)
    email = models.EmailField(max_length=30,unique=True)
    created_time_stamp = models.DateTimeField(auto_now_add=True)
    update_by_time_stamp = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, blank=True)
    is_admin = models.BooleanField(default=False, blank=True)

    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELD = []

