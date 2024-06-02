from django.db import models

# Create your models here.
class Person(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)