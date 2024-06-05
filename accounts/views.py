from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Student, School
from .forms import StudentForm, LoginForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully')
            return redirect(reverse('login'))
        else:
            messages.error(request, 'Error in form submission')
            print('an error occurred')
            print(form.errors)
    form = StudentForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            messages.error(request, 'Error in form submission')
            print(form.errors)
            return render(request, 'accounts/login.html', {'form': form})
        username = form.cleaned_data.get('username')
        print(username)
        password = form.cleaned_data.get('password')
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful')
            print(request.user)
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'accounts/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    messages.success(request, 'Logout successful')
    return redirect(reverse('login'))