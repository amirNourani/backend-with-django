from django.shortcuts import render
from foods.models import Food


# Create your views here.
def menu(request):
    food = Food.objects.all()
    
    context= {
        'foods': food
    }
    
    return render(request, 'menu/menu.html', context)
