from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Food(models.Model):
    FOOD_TYPE = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('drinks', 'Drinks'),
    ]
    name = models.CharField(max_length= 30)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    photo_food = models.ImageField(upload_to = 'foods/')
    food_type = models.CharField(max_length= 9, choices= FOOD_TYPE, default='drinks')
    
    def __str__(self):
        return self.name