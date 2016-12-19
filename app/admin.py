from django.contrib import admin        # register your models here
from .models import Customer, Order

admin.site.register(Customer)
admin.site.register(Order)
