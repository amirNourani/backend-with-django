import re
from django.shortcuts import render
from .models import Stuff
# Create your views here.
def stuff(request):
    stuff = Stuff.objects.all()
    
    
    return render(request, 'stuff/stuff.html', {'stuffs': stuff})