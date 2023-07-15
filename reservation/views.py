import re
from django.shortcuts import render

from .forms import ReservationForm

# Create your views here.

def reserve(request):
    reservation = ReservationForm()
    if request.method == "POST":
        reservation = ReservationForm(request.POST)
        if reservation.is_valid():
            reservation.save()
    else:
        reservation = ReservationForm()
        
    context = {
        'reserve': reservation
    }
    
    return render(request, 'reservation/reservation.html', context)