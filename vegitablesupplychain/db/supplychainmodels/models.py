# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
    GENDER = (("MALE", "MALE"),
              ("FEMALE", "FEMALE"))
    username = models.CharField(max_length=255, primary_key=True)
    fname = models.CharField(max_length=512)
    mname = models.CharField(max_length=512)
    lname = models.CharField(max_length=512)
    mobile = models.CharField(max_length=12)
    gender = models.CharField(max_length=512, choices=GENDER)
    address = models.ForeignKey(Address)


class Farmer(models.Model):
    user = models.ForeignKey(User)


class Hotel(models.Model):
    user = models.ForeignKey(User)
    hotel_name = models.CharField(max_length=512)
    gst_no = models.CharField(max_length=20, primary_key=True)


class Category(models.Model):
    name = models.CharField(max_length=255, primary_key=True)


class Product(models.Model):
    name = models.CharField(max_length=512)
    category = models.ForeignKey(Category)
    default_image = models.CharField(max_length=512, null=True)

