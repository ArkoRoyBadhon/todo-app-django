from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django import forms
# Create your models here.
class CR(models.Model): 
    username = models.ForeignKey(User, on_delete=models.CASCADE) 
class TODO(models.Model):     
    title = models.CharField(max_length=250)
    about=models.TextField(max_length=450,null=True)    
    course = models.CharField(max_length=125,null=True )    
    date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_date = models.DateField(null=True)
    end_time = models.TimeField(null=True)
    url1=models.URLField(max_length = 200,null=True)
    url2=models.URLField(max_length = 200,null=True)
    w1 = models.CharField(max_length=30,null=True)
    w2 = models.CharField(max_length=30,null=True)
 
 