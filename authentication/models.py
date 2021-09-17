# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.forms import UserCreationForm

class mobile(models.Model):
    sId=models.IntegerField()
    phone=models.CharField(max_length=50)
class business(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
class Meta:
    db_table = "django"
    model = mobile
    model = business
    fields = [
          'sId',
          'phone',
      ]
    fields = [
          
          'phone',
          'name'
      ]
# Create your models here.
