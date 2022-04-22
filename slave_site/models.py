from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Product(models.Model):
    label = models.CharField(max_length=20)
    price = models.IntegerField()
    url_img = models.URLField()
    id_user = models.IntegerField()