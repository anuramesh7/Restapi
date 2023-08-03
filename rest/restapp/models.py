from django.db import models

# Create your models here.
class ride(models.Model):
    rider=models.CharField(max_length=200)
    driver = models.CharField(max_length=200)
    date_Created = models.DateField(auto_now=True)
    pickup_loc=models.CharField(max_length=200)
    status_completed=models.BooleanField(default=False)
    dropoff_loc = models.CharField(max_length=200,default=False)
    status = models.CharField(max_length=50, default='pending')

