from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Covers(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    discount = models.IntegerField()


class customer(models.Model):
    name = models.CharField(max_length=50)
    relation = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=False)


