from django.shortcuts import render
from django.http import HttpResponse
from .models import Ex_Routines
import math
# Create your views here.

def blog(request):
    return render(request, 'Blog/index.html')

def index(request):
    return render(request, 'GymFreak/index.html')

def Ex_Routines(request):
    allProds = []
    catprods = Ex_Routines.objects.values('category', 'routine_id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Ex_Routines.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'Ex_Routines/index.html', params)