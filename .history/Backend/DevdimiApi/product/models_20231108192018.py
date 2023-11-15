from django.db import models

class Product(models.Model):
    name = models.CharField()
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    

# Create your models here.
