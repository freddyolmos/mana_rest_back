from django.db import models

# Create your models here.

class Food(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=200)
    image = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)

    def __str__(self):
        return f"{self.title}"
    

class Store(models.Model):
    user = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    foods = models.ForeignKey(Food, on_delete=models.CASCADE)