from django.db import models

# Create your models here.
class Reading(models.Model):
    location = models.CharField(max_length=100)
    weather = models.CharField(max_length=20)
    wind_str = models.CharField(max_length=100)
    temp = models.IntegerField()
    humidity = models.CharField(max_length=10)
    precip = models.CharField(max_length=50)
    icon_url = models.URLField()
    observation_time = models.CharField(max_length=100)

class Users(models.Model):
    us_name = models.CharField(max_length=64, default='')
    us_password = models.CharField(max_length=64, default='')
    us_loggedin = models.BooleanField(default=False)

class Lists(models.Model):
    li_name = models.CharField(max_length=64, default='')
    li_username = models.CharField(max_length=64, default='')

class Order(models.Model):
    or_product = models.CharField(max_length=256, default='')
    or_amount = models.CharField(max_length=256, default='')
    or_listid = models.IntegerField(default=0)