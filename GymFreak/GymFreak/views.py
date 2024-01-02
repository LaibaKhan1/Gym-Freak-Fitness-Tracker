from django.shortcuts import render
from django.http import HttpResponse
from .models import ex_routines
from math import ceil
# Create your views here.

def blog(request):
    return render(request, 'Blog/index.html')

def index(request):
    return render(request, 'GymFreak/index.html')

# def Ex_Routines(request):
#     allProds = []
#     catprods = ex_routines.objects.values('category', 'id')
#     cats = {item['category'] for item in catprods}
#     for cat in cats:
#         prod = ex_routines.objects.filter(category=cat)
#         n = len(prod)
#         nSlides = n // 4 + math.ceil((n / 4) - (n // 4))
#         allProds.append([prod, range(1, nSlides), nSlides])
#     params = {'allProds':allProds}
#     return render(request, 'Ex_Routines/index.html', params)

def Ex_Routines(request):
    # Get all unique categories
    categories = ex_routines.objects.values_list('category', flat=True).distinct()

    # Organize data for each category
    allProds = []
    for category in categories:
        products = ex_routines.objects.filter(category=category)
        range_values = range(products.count())
        nSlides = nSlides = (len(products) // 4) + ceil((len(products) / 4) - (len(products) // 4))
        allProds.append((products, range_values, nSlides))

    return render(request, 'Ex_Routines/index.html', {'allProds': allProds})