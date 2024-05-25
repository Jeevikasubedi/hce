from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=10)
    Adress=models.TextField()
    phone=models.IntegerField()



    def __str__(self):
        return self.name 
# Create your models here.
