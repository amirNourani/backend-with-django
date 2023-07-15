from django.shortcuts import render
from django.urls import conf
from .models import Food

# Create your views here.
def index(request):
    food_list = Food.objects.all()
    
    context = {
        'foods': food_list
    }
    
    return render(request, 'foods/index.html', context)