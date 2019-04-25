# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models


# Create your models here.

class Address(models.Model):
    address_line1 = models.CharField(max_length=512)
    address_line2 = models.CharField(max_length=512)
    state = models.CharField(max_length=512, null=False)
    district = models.CharField(max_length=512, null=False)
    taluka = models.CharField(max_length=512, null=False)
    village = models.CharField(max_length=512, null=True)
    pincode = models.CharField(max_length=20, null=True)


class User(models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=1024)
    created_on = models.DateTimeField(auto_now=True)
    fullname = models.CharField(max_length=512)
    mobile = models.CharField(max_length=12)
    pan_no = models.CharField(max_length=12)
    account_no = models.CharField(max_length=15)
    shipping_addresses = models.ManyToManyField(Address)
    photo = models.CharField(max_length=1024, null=True)


class Farmer(models.Model):
    user = models.ForeignKey(User)


class Hotel(models.Model):
    user = models.ForeignKey(User)
    hotel_name = models.CharField(max_length=512)
    gstn_no = models.CharField(max_length=20, primary_key=True)


class Login(models.Model):
    user = models.ForeignKey(User)
    login_token = models.CharField(max_length=70, default=str(uuid.uuid4()),
                                   primary_key=True)
    created_on = models.DateTimeField(auto_now_add=True)
    loggedout_time = models.DateTimeField(null=True)
    is_logged_in = models.BooleanField(default=True)


class Category(models.Model):
    category_name = models.CharField(max_length=255, primary_key=True)


class Brand(models.Model):
    brand_name = models.CharField(max_length=255, primary_key=True)


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    brand = models.ForeignKey(Brand)
    default_image = models.CharField(max_length=512, null=True)
    features = models.CharField(max_length=512, null=True)
    price = models.FloatField(max_length=10, null=False)


class SellOrders(models.Model):
    sell_order_token = models.CharField(max_length=70,
                                        default=str(uuid.uuid4()),
                                        primary_key=True)
    farmer = models.ForeignKey(Farmer)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField()
    product_image = models.CharField(max_length=512)
    order_status = models.CharField(max_length=10,default=str('In Stock'))
    is_shipped = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    shipping_address = models.ForeignKey(Address)


class CartItem(models.Model):
    sell_order = models.ForeignKey(SellOrders)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)


class Cart(models.Model):
    hotel = models.ForeignKey(Hotel)
    cart_items = models.ManyToManyField(CartItem)
    created_on = models.DateTimeField(auto_now_add=True)
    total_item_price = models.FloatField()
    is_active = models.BooleanField(default=True)


class PurchaseOrders(models.Model):
    purchase_order_token = models.CharField(max_length=70,
                                            default=str(uuid.uuid4()),
                                            primary_key=True)
    hotel = models.ForeignKey(Hotel)
    cart = models.ForeignKey(Cart)
    total_price = models.FloatField(max_length=10, null=False)
    is_shipped = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    shipping_address = models.ForeignKey(Address)
