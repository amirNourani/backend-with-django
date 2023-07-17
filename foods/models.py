from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
class Food(models.Model):
    name = models.CharField(max_length= 200)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    photo_food = models.ImageField(upload_to = 'foods/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="category", null=True)
    is_suggested = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name
    
    
