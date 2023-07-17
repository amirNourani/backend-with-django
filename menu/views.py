from django.shortcuts import render
from foods.models import Food, Category


# Create your views here.
def menu(request):
    foods_list = Food.objects.all().order_by('category')
    categorys = Category.objects.all()
    context= {
        'foods_list': foods_list,
        'categorys': categorys
    }
    
    return render(request, 'menu/index.html', context)