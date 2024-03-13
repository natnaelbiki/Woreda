# views.py

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')  # Replace 'login' with the URL name of your login page
    else:
        return render(request, 'registration/login.html')  # Replace 'login.html' with the template for your login page


def custom_logout(request):
    logout(request)
    return redirect('login')