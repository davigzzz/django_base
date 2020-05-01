from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
#from estructura.models import Usuario


# Create your views here.
@login_required()
def home(request):
    return render(request, 'bienes/home.html', {})

