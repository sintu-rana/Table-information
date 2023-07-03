from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    age=models.IntegerField()
    pic=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
    