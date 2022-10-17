from django.db import models
#from django.contrib.auth.models import AbstractUser

# name: a short string that identifies a thing.
# description: a slightly longer string that describes a thing.
# quantity: an integer that identifies the number of items of a thing we possess.

class Thing(django.db.models.Model):

    name = models.TextField()
    description = models.TextField()
    quantity = models.TextField()

    #test