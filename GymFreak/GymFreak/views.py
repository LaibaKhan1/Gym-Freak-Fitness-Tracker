from django.shortcuts import render
from django.http import HttpResponse
from .models import ex_routines
from math import ceil
import requests
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

def calculate_calories(food_name):
    # Replace 'YOUR_APP_ID' and 'YOUR_APP_KEY' with your Edamam API credentials
    app_id = 'API signup'
    app_key = '7fa82f0a'
    
    # Edamam API endpoint
    api_endpoint = 'https://api.edamam.com/api/nutrition-details'
    
    # Prepare the request payload
    payload = {
        'app_id': app_id,
        'app_key': app_key,
    }

    # The 'ingr' parameter should contain the food name
    data = {
        'ingr': [food_name],
    }

    # Make the API request
    response = requests.post(api_endpoint, params=payload, json=data)

    # Parse the response
    if response.status_code == 200:
        result = response.json()
        # Extract calories from the API response
        calories = result.get('calories', {}).get('total', 0)
        return calories
    else:
        # Handle API errors
        return None

def Meal_Tracker(request):
    if request.method == 'POST':
        breakfast_diet = request.POST.get('breakfast_diet', '')
        lunch_diet = request.POST.get('lunch_diet', '')
        dinner_diet = request.POST.get('dinner_diet', '')

        # Calculate calories for each meal
        breakfast_calories = calculate_calories(breakfast_diet)
        lunch_calories = calculate_calories(lunch_diet)
        dinner_calories = calculate_calories(dinner_diet)

        # Calculate total calories
        total_calories = breakfast_calories + lunch_calories + dinner_calories

        return render(request, 'Meal_Tracker/index.html', {'thank': True, 'total_calories': total_calories})

    return render(request, 'Meal_Tracker/index.html', {'thank': False})