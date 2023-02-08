from django.db import models

# Create your models here.


class Covers(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    discount = models.IntegerField()
