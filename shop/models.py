from typing import Match
from django.db import models
from django.utils.timezone import  datetime

# Create your models here.
class  Product(models.Model):
     product_id = models.AutoField
     product_name = models.CharField(max_length=50)
     category = models.CharField(max_length=50)
     sub_category = models.CharField(max_length=50)
     price = models.IntegerField(default=0)
     desc = models.CharField(max_length=50)
     pub_date = models.DateField()
     image = models.ImageField(upload_to = 'shop/images')
     
     def __str__(self):
          return self.product_name
     
class Orders(models.Model):
     order_id = models.AutoField(primary_key=True)
     items_json = models.CharField(max_length=5000)
     name = models.CharField(max_length=50)
     email = models.CharField(max_length=50)
     address = models.CharField(max_length=100)
     city = models.CharField(max_length=50)
     state = models.CharField(max_length=50)
     zip_code = models.CharField(max_length=50)
     phone = models.CharField(max_length=50)
     order_date = models.DateTimeField(default=datetime.now,blank=True)

class OrderUpdates(models.Model):
     update_id = models.AutoField(primary_key=True)  
     order_id= models.IntegerField(default="")
     update_desc = models.CharField(max_length=200)
     timestamp = models.DateField(auto_now_add=True)

     def __str__(self):
          return self.update_desc[0:7]+"...."