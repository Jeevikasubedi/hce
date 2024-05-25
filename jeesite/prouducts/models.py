from django.db import models

# Create your models here.
from django.db import models 
from categories.models import Category
class Products(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()

    def __str__(self):
         return self.name