from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=200, null=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    role=models.CharField(max_length=200, default='user')

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name', 'last_name', 'password']

    objects=UserManager()


# class Register(models.Model):
#     email = models.EmailField(unique=True)
#     password= models.CharField(max_length=8, null=True)
#     age=models.IntegerField()
#     origin=models.CharField(max_length=250)
#     gender=models.CharField(max_length=250)
#     phone=models.CharField(max_length=15)



# class UserList(models.Model):
#     user = models.ForeignKey(Register, on_delete=models.CASCADE)

class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

