# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
import os



# Create your models here.
class Car (models.Model):

    make = models.CharField(max_length = 150)
    Type = models.CharField(max_length= 150)
    year = models.CharField(max_length = 100)
    colour= models.CharField(max_length= 100)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    image = models.ImageField(null=True, blank=True,
    height_field="height_field",
    width_field="width_field" )
    height_field= models.IntegerField(default=0)
    width_field= models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add= True)



    def __str__(self):
        return str(self.make)
