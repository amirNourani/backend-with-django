from django.shortcuts import render
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='login:login')
def reserve(request):
    form = ReservationForm()
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Your reservation is successfully done.")
            form.save()
        else:
            messages.error(request, "Unsuccessful reservation. Invalid information.")
    return render(request, 'reservation/index.html', {'form': form})            