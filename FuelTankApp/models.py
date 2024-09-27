from django.db import models
from datetime import datetime ,date
from django.utils import timezone

    
    


class HoleDB(models.Model):
    azone=models.CharField(max_length=10)
    bzone=models.CharField(max_length=10)
    czone=models.CharField(max_length=10)
    dzone=models.CharField(max_length=10)
    ezone=models.CharField(max_length=10)
    fzone=models.CharField(max_length=10)
    gzone=models.CharField(max_length=10)
    DateTime = models.DateTimeField(default=datetime.now,blank=False)





class FuelTankLeakTestDB(models.Model):
    azone=models.CharField(max_length=10,blank=True,null=True,default=0)
    bzone=models.CharField(max_length=10,blank=True,null=True,default=0)
    czone=models.CharField(max_length=10,blank=True,null=True,default=0)
    d1zone=models.CharField(max_length=10,blank=True,null=True,default=0)
    d2zone=models.CharField(max_length=10,blank=True,null=True,default=0)
    ezone=models.CharField(max_length=10,blank=True,null=True,default=0)
    fzone=models.CharField(max_length=10,blank=True,null=True,default=0)
    gzone=models.CharField(max_length=10,blank=True,null=True,default=0)
    DateTime = models.DateTimeField(default=datetime.now,blank=False)
