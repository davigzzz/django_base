from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_view(request):
    usuario = request.POST.get('usuario')
    password = request.POST.get('password')
    user = authenticate(request, usuario = usuario, password = password)
    print(user)
    if user is not None:
        login(request, user)
        return redirect("home")
    else:
        return render(request, 'estructura/login.html', {})

def logout_view(request):
    logout(request)
    return render(request, 'estructura/login.html', {})

@login_required()
def home(request):
    if request.user.is_authenticated():
        print("Logged in")
    else:
        print("Not logged in")
    print("HOOOLA")
    return render(request, 'bienes/home.html')