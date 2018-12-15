# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class details(models.Model):
    FirstName=models.CharField(max_length=30,null=False)
    LastName=models.CharField(max_length=30,null=False)
    Email=models.EmailField(max_length=30,null=False)
    AccountNumber=models.IntegerField(max_length=30,null=False)
    Location=models.CharField(max_length=30,null=False)

    def __str__(self):
        return self.FirstName