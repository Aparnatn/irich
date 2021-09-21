# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.forms import UserCreationForm
import datetime
import os


class mobile(models.Model):
    sId=models.IntegerField()
    phone=models.CharField(max_length=50)
class business_details(models.Model):
    category=models.CharField(max_length=100)
    bank_name=models.CharField(max_length=50)
    bsb=models.CharField(max_length=50)
    business_name=models.CharField(max_length=50)
    business_desc=models.CharField(max_length=200)
    business_address=models.CharField(max_length=200)
    email=models.EmailField(max_length=50)
    Abin=models.CharField(max_length=50)
    subcategory=models.CharField(max_length=50)
    Account_holder=models.CharField(max_length=50)
    account_number=models.CharField(max_length=50)
    
    image1= models.ImageField(upload_to='images',blank= True,null=True)
class transactions(models.Model):
    transactionId = models.AutoField(primary_key=True)
    transactionName = models.CharField(max_length=500)
class Meta:
    db_table = "django"
    model = mobile
    model = business_details
    model = transactions
    fields = [
          'sId',
          'phone',
      ]
    fields = [
          ' transactionId',
          'transactionName',
      ]
    fields = [
          
         'category',
         'bank_name',
          'bsb',
            'business_name',
            'business_desc',
            'business_address',
            'email',
            'Abin',
            'subcategory',
            'Account_holder',
            'account_number',
            'image1',
            
      ]
# Create your models here.
