from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=32)
    quantity = models.IntegerField()
    price = models.FloatField()
    description = models.CharField(max_length=128)
    image = models.URLField(max_length=200)

class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    online = models.BooleanField
    email = models.EmailField
