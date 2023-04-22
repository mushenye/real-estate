from django.db import models

# Create your models here.
class Listing(models.Model):
    title= models.CharField(max_length=100)
    price= models.IntegerField()
    num_beds=models.IntegerField()
    address=models.CharField(max_length= 100)
     
    def __str__(self):
        return self.title