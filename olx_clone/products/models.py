from django.db import models


# Create your models here.
class Product(models.Model):
    seller_name = models.CharField(max_length=100)
    seller_number = models.IntegerField(max_length=13)
    product_title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

def __str__(self):
    return self.name
