from django.db import models

# Create your models here.

class studentdb(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    place=models.CharField(max_length=100, null=True, blank=True)
    age=models.IntegerField(null=True, blank=True)
    email=models.EmailField(null=True, blank=True)

class employeedb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
