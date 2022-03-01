from django.db import models
from typing import Match
from django.db import models

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,default = "")
    head0 = models.CharField(max_length=50,default = "")
    c_head0 = models.CharField(max_length=5000,default = "")
    head1 = models.CharField(max_length=50,default = "")
    c_head1 = models.CharField(max_length=5000,default = "")
    head2 = models.CharField(max_length=50,default = "")
    c_head2 = models.CharField(max_length=5000,default = "")
    author_name = models.CharField(max_length=50,default = "")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to = 'blogs/images',default = "")
     
    def __str__(self):
          return self.title


