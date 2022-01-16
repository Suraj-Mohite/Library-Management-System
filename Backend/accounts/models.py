from django.db import models
from accounts.managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(db_index=True,unique=True,max_length=254)
    first_name=models.CharField(max_length=240)
    last_name=models.CharField(max_length=240)

    is_staff=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)

    objects=CustomUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'