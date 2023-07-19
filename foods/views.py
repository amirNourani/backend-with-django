from django.shortcuts import render
from .models import Food, Category

# Create your views here.
def index(request):
    is_suggested = True
    food_list = Food.objects.filter(is_suggested = is_suggested).order_by('category')
    categorys = Category.objects.all()

    context = {
        'foods_list': food_list,
        'categorys': categorys,
        'is_suggested': is_suggested
        
    }
    return render(request, 'foods/index.html', context)