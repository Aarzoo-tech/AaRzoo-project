from django.db import models
from django.contrib.auth.models import *
class social_contest(models.Model):
    Que=models.CharField(max_length=100)
    opt1=models.CharField(max_length=50)
    opt2=models.CharField(max_length=50)
    opt3=models.CharField(max_length=50)
    opt4=models.CharField(max_length=50)
    ans=models.CharField(max_length=50,default='')
class registration(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    cnfpswd=models.CharField(max_length=50)
class UserLogin(models.Model):
    username=models.OneToOneField(registration,on_delete=models.CASCADE)
    password=models.OneToOneField(registration,on_delete=models.CASCADE)