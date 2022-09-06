from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=12)
    is_staff = models.BooleanField()