from django.shortcuts import render
from django.http import HttpResponse
from .models import ex_routines
from math import ceil
import requests
from collections.abc import MutableMapping
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
    categories = ex_routines.objects.values_list('category', flat=True).distinct()

    allProds = []
    for category in categories:
        products = ex_routines.objects.filter(category=category)
        range_values = range(products.count())
        nSlides = nSlides = (len(products) // 4) + ceil((len(products) / 4) - (len(products) // 4))
        allProds.append((products, range_values, nSlides))

    return render(request, 'Ex_Routines/index.html', {'allProds': allProds})

def calculate_calories(food_name):
    app_id = '7fa82f0a'
    app_key = 'a216df8f46fbd7fde9b7f71d4b650f90'
    
    api_endpoint = 'https://api.edamam.com/api/nutrition-details'
    
    payload = {
        'app_id': app_id,
        'app_key': app_key,
    }

    data = {
        'ingr': [food_name],
    }

    response = requests.post(api_endpoint, params=payload, json=data)

    if response.status_code == 200:
        result = response.json()

        if isinstance(result['calories'], int):
            return None

        if 'calories' in result and 'total' in result['calories']:
            calories = result['calories']['total']
            return calories
        else:
            return None
    else:
        return None

# def Meal_Tracker(request):
#     if request.method == 'POST':
#         breakfast_diet = request.POST.get('breakfast_diet', '')
#         lunch_diet = request.POST.get('lunch_diet', '')
#         dinner_diet = request.POST.get('dinner_diet', '')

#         # Calculate calories for each meal using the Edamam API
#         breakfast_calories = calculate_calories(breakfast_diet)
#         lunch_calories = calculate_calories(lunch_diet)
#         dinner_calories = calculate_calories(dinner_diet)

#         # Check if any of the API calls failed
#         if None in [breakfast_calories, lunch_calories, dinner_calories]:
#             # Handle the case where one or more API requests failed
#             return render(request, 'Meal_Tracker/index.html', {'thank': False})

#         # Calculate total calories
#         total_calories = breakfast_calories + lunch_calories + dinner_calories

#         # Pass total_calories to the template, and set thank to True
#         return render(request, 'Meal_Tracker/index.html', {'thank': True, 'total_calories': total_calories})

#     return render(request, 'Meal_Tracker/index.html', {'thank': False})


def Meal_Tracker(request):
    if request.method == 'POST':
        breakfast_diet = request.POST.get('breakfast_diet', '')
        lunch_diet = request.POST.get('lunch_diet', '')
        dinner_diet = request.POST.get('dinner_diet', '')

        breakfast_calories = calculate_calories(breakfast_diet)
        lunch_calories = calculate_calories(lunch_diet)
        dinner_calories = calculate_calories(dinner_diet)

        if None in [breakfast_calories, lunch_calories, dinner_calories]:
            print("API request failed")
            return render(request, 'Meal_Tracker/index.html', {'thank': False})

        total_calories = breakfast_calories + lunch_calories + dinner_calories

        print("Total Calories:", total_calories)

        return render(request, 'Meal_Tracker/index.html', {'thank': True, 'total_calories': total_calories})

    return render(request, 'Meal_Tracker/index.html', {'thank': False})