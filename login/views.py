from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.

def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password.")
        else: 
            messages.error(request,"Invalid username or password.")
            return redirect('/login') 
    form = LoginForm()
    context= {
        'form': form
    }
    return render(request, 'login/index.html', context)

def logout_user(request):
    logout(request)
    return redirect("login:login")

def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'login/register.html', context)