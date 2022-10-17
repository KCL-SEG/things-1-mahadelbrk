from enum import unique
from django.core.validators import MinValueValidator, MaxValueValidator
from wsgiref.validate import validator
from django.db import models
#from django.contrib.auth.models import AbstractUser

# name: a short string that identifies a thing.
# description: a slightly longer string that describes a thing.
# quantity: an integer that identifies the number of items of a thing we possess.

class Thing(models.Model):

    name = models.CharField(unique=True, blank=False, max_length= 30)
    description = models.CharField(unique=False, blank=True, max_length= 120)
    quantity = models.IntegerField(unique=False, validators= [MinValueValidator(0), MaxValueValidator(100)])