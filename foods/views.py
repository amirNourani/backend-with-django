from django.shortcuts import render
from .models import Food, Category

# Create your views here.
def index(request):
    food_list = Food.objects.filter(is_suggested = True).order_by('category')
    categorys = Category.objects.all()

    context = {
        'foods_list': food_list,
        'categorys': categorys,
    }
    
    return render(request, 'foods/index.html', context)