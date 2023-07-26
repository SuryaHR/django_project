from django.db import models

# Create your models here.

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=30)
    restaurant_image = models.ImageField(upload_to='media',default='')


    def __str__(self):
        return self.restaurant_name
    
class Food(models.Model):
    food_name = models.CharField(max_length=30)
    restaurants = models.ManyToManyField(Restaurant)
    food_image = models.ImageField(upload_to='media',default='')

    def __str__(self):
        return self.food_name

