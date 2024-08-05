from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, is_staff=False, is_superuser=False, **extra_fields):
        user = self.model(email=email, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        return self.create_user(email, password, is_staff=True, is_superuser=True, **extra_fields)


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='user_images')

    objects = CustomUserManager
    USERNAME_FIELD = ['email']

    def __str__(self) -> str:
        return self.first_name






