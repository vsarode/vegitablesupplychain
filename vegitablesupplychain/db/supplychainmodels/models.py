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
    name = models.CharField(max_length=512)
    mobile = models.CharField(max_length=12)
    pan_no = models.CharField(max_length=12)
    account_no = models.CharField(max_length=15)
    user_type = models.CharField(max_length=512,)
    address = models.ForeignKey(Address)
    photo = models.CharField(max_length=1024, null=True)


class Farmer(models.Model):
    user = models.ForeignKey(User)


class Hotel(models.Model):
    user = models.ForeignKey(User)
    hotel_name = models.CharField(max_length=512)
    gst_no = models.CharField(max_length=20, primary_key=True)


class Login(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=70, default=str(uuid.uuid4()), primary_key=True)
    created_on = models.DateTimeField(auto_now=True)
    loggedout_time = models.DateTimeField(null=True)
    is_logged_in = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=255, primary_key=True)


class Product(models.Model):
    name = models.CharField(max_length=512)
    category = models.ForeignKey(Category)
    default_image = models.CharField(max_length=512, null=True)

class WareHouse(models.Model):
    name = models.CharField(max_length=254,primary_key=True)
    address = models.ForeignKey(Address)


class FarmerProductDetails(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(max_length=10,null=False)
    warehouse = models.ForeignKey(WareHouse)
    min_price = models.FloatField(max_length=10,null=False)
    max_price = models.FloatField(max_length=10, null=False)

