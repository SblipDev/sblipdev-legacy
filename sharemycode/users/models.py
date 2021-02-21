from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    description = models.TextField()
    role = models.CharField(max_length=200)

