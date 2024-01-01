from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog(request):
    return render(request, 'Blog/index.html')

def index(request):
    return render(request, 'GymFreak/index.html')

def ex_routines(request):
    return render(request, 'Ex_Routines/index.html')