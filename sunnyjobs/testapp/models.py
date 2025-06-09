from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=60)
    title=models.CharField(max_length=60)
    eligibility=models.CharField(max_length=60)
    address=models.CharField(max_length=70)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()

class puneJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=60)
    title=models.CharField(max_length=60)
    eligibility=models.CharField(max_length=60)
    address=models.CharField(max_length=70)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()

class bangloreJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=60)
    title=models.CharField(max_length=60)
    eligibility=models.CharField(max_length=60)
    address=models.CharField(max_length=70)
    email=models.EmailField()
    phonenumber=models.BigIntegerField()