from enum import unique
from django.core.validators import MinValueValidator, MaxValueValidator
from wsgiref.validate import validator
from django.db import models
#from django.contrib.auth.models import AbstractUser

# name: a short string that identifies a thing.
# description: a slightly longer string that describes a thing.
# quantity: an integer that identifies the number of items of a thing we possess.

class Thing(models.Model):

    name = models.CharField( max_length= 30, unique=True, blank=False)
    description = models.CharField(max_length= 120, blank=True)
    quantity = models.IntegerField( validators= [MinValueValidator(0), MaxValueValidator(100)])