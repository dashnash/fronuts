from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=48)

    def __str__(self):
        return self.name
    
class Shop(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Fronut(models.Model):
    user = models.ForeignKey(User)
    shop = models.ForeignKey(Shop)
    date = models.DateTimeField('date brought')
    initial_amount = models.IntegerField(default=12)
    remaining_amount = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return "{0} - {1}".format(self.user.name, self.shop.name)