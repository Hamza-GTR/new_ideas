from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Covers(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()


class Customer(models.Model):
    name = models.CharField(max_length=50)
    relation = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=False)


class ProductDetails(models.Model):
    features = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    discount = models.IntegerField()


class Products(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    details = models.ForeignKey(ProductDetails, on_delete=models.CASCADE, default=None)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    status = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    amount = models.IntegerField(default=None, blank=True, null=True)


class Shipping_Address(models.Model):
    ship_adr = models.ForeignKey(Order, on_delete=models.CASCADE, default=None)
    Street = models.CharField(max_length=30, default=None)
    City = models.CharField(max_length=30, default=None)
    State = models.CharField(max_length=30, default=None)
    PostalCode = models.PositiveIntegerField(default=None)
    Country = models.CharField(max_length=30, default=None)
    phoneNumber = models.IntegerField(default=None)


class Order_Items(models.Model):
    product = models.ForeignKey(Products, related_name='s_product', on_delete=models.CASCADE, default=None)
    order = models.ForeignKey(Order, related_name='s_order', on_delete=models.CASCADE, default=None)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    Date = models.DateTimeField(auto_now_add=True)
