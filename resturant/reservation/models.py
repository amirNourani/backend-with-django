from django.db import models


# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length= 50)
    email = models.EmailField()
    phone = models.CharField(max_length= 15)
    date = models.DateField()
    time = models.TimeField()
    person = models.IntegerField()
    
    class Meta:
        ordering = ('date', 'time')
    
    def __str__(self):
        return self.name.title()