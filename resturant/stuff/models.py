from django.db import models

# Create your models here.
class Stuff(models.Model):
    name = models.CharField(max_length= 50) 
    job = models.CharField(max_length= 50)
    image = models.ImageField(upload_to = 'stuffs')
    
    def __str__(self):
        return self.name.title()