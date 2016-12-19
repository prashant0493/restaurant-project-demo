from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Order(models.Model):
    FoodItem = models.CharField(max_length=50)
    Price =  models.CharField(max_length=50)

    def __str__(self):
        return str(self.FoodItem) 



class Customer(models.Model):
    Name = models.CharField(max_length=200)  
    Password = models.CharField(max_length=50)    
    Contact = models.CharField(max_length=10)         
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Created_date = models.DateTimeField(default=timezone.now)
    Feedback = models.TextField(default=None)

    def place_order(self):
        self.Created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.Name) + str(self.Contact)

    
