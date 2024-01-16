from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
# User = get_user_model()

# Create your models here.

class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    is_visitor = models.BooleanField(default=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)


class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    

class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    