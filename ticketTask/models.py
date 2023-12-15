from django.db import models

# Create your models here.
class CoffeeShop(models.Model):
   coffeeName = models.CharField(max_length=255)
   coffeeDesc = models.TextField()
   coffeePrice = models.DecimalField(max_digits=10, decimal_places=2)
   coffeeFlavor = models.CharField(max_length=100)
   isWithMarshmello = models.BooleanField(default=False)
   isWithDonuts = models.BooleanField(default=False)
   isAvailable = models.BooleanField(default=True)
   coffeeSize = models.CharField(max_length=50)


   def __str__(self):
      return self.coffeeName

