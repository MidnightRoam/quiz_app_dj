from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.contrib.auth.models import User
from django.db import IntegrityError


class LoginView(View):
    """User login functionality using built-in Django tools"""
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, 'users/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('/')
        return render(request, 'users/login.html')


class SignupView(View):
    """User registration functionality using built-in Django tools"""
    def get(self, request):
        return render(request, 'users/registration.html')

    def post(self, request):
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        existing_user = User.objects.filter(username=username).exists()
        if existing_user:
            context = {'error': 'A user with this username already exists.'}
            return render(request, 'users/registration.html', context=context)

        if password1 != password2 or not username:
            context = {'error': 'Please enter a valid username and make sure that the passwords match.'}
            return render(request, 'users/registration.html', context=context)

        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        return redirect('/')


class LogoutView(View):
    """User logout functionality using built-in Django tools"""
    def get(self, request):
        logout(request)
        return redirect('/')
