from django.contrib.auth.forms import AuthenticationForm as LoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect, render
from django.http import HttpRequest

from auth.forms import RegistrationForm

def signin(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect(reverse('main:main'))

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return redirect(reverse('main:main'))
        else:
            form = LoginForm()
            return render(request, 'auth/signin.html', {"form": form})

    else:
        form = LoginForm()
        return render(request, 'auth/signin.html', {"form": form})


def signup(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect(reverse('main:main'))

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('main:main'))

        else:
            return render(request, 'auth/signup.html', {"form": form})

    else:
        form = RegistrationForm()
        return render(request, 'auth/signup.html', {"form": form})


def logout_user(request: HttpRequest):
    logout(request)
    
    return redirect(reverse('main:main'))