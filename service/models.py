from django.db import models

# Create your models here.
class Signup(models.Model):
    fname=models.CharField(max_length=20)
    address=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    mobile=models.CharField(max_length=20)
    pass1=models.CharField(max_length=20)
    repass=models.CharField(max_length=20)
    gen=models.CharField(max_length=20)
 
class Flight(models.Model):
    fid=models.IntegerField()
    dt1=models.CharField(max_length=30)
    fname=models.CharField(max_length=30)
    seats=models.IntegerField()
    source=models.CharField(max_length=30)
    dest=models.CharField(max_length=30)
    prize=models.IntegerField()
    dt2=models.CharField(max_length=30)
    
class reservation(models.Model):
    bid=models.IntegerField()
    dt=models.CharField(max_length=30)
    name =models.CharField(max_length=30)
    email =models.CharField(max_length=30)
    mobile =models.CharField(max_length=30)
    fname =models.CharField(max_length=30)
    bookdt =models.CharField(max_length=30)
    source =models.CharField(max_length=30)
    dest =models.CharField(max_length=30)
    seat=models.IntegerField()
    prize=models.IntegerField()
    status=models.CharField(max_length=30,default='reserve')
