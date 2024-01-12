from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ex_routines, CalorieEntry, CaloriesBurned, LoginPageSettings
from .forms import CalorieBurnedEntryForm, CalorieEntryForm
from math import ceil
import requests
from .forms import CalorieEntryForm
# Create your views here.

def blog(request):
    return render(request, 'Blog/index.html')

def index(request):
    return render(request, 'GymFreak/index.html')

def login(request):
    login_page_settings = LoginPageSettings.objects.first()
    return render(request, 'login_page.html', {'login_page_settings': login_page_settings})

def signup(request):
    login_page_settings = LoginPageSettings.objects.first()
    return render(request, 'signup/index.html', {'login_page_settings': login_page_settings})

def Ex_Routines(request):
    categories = ex_routines.objects.values_list('category', flat=True).distinct()

    allProds = []
    for category in categories:
        products = ex_routines.objects.filter(category=category)
        range_values = range(products.count())
        nSlides = nSlides = (len(products) // 4) + ceil((len(products) / 4) - (len(products) // 4))
        allProds.append((products, range_values, nSlides))

    return render(request, 'Ex_Routines/index.html', {'allProds': allProds})

def exerciseView(request, myid):
    exercise = ex_routines.objects.filter(id=myid)
    return render(request, 'Ex_Routines/exeview.html', {'product': exercise[0]})

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
        if 'calories' in result:
            if isinstance(result['calories'], int):
                total_calories = result['calories']
                return [total_calories]
            elif 'total' in result['calories']:
                total_calories = result['calories']['total']
                if total_calories is not None:
                    total_calories = int(total_calories)
                    return [total_calories]
        return [None]
    else:
        print("API Request Failed. Status Code:", response.status_code)
        return [None]

def Meal_Tracker(request):
    if request.method == 'POST':
        breakfast_diet = request.POST.get('breakfast_diet', '')
        lunch_diet = request.POST.get('lunch_diet', '')
        dinner_diet = request.POST.get('dinner_diet', '')

        breakfast_calories = calculate_calories(breakfast_diet)
        lunch_calories = calculate_calories(lunch_diet)
        dinner_calories = calculate_calories(dinner_diet)

        if None in [breakfast_calories, lunch_calories, dinner_calories]:
            return render(request, 'Meal_Tracker/index.html', {'thank': False})

        total_calories = sum([calories[0] for calories in [breakfast_calories, lunch_calories, dinner_calories] if calories is not None])

        return render(request, 'Meal_Tracker/index.html', {'thank': True, 'total_calories': total_calories})

    return render(request, 'Meal_Tracker/index.html', {'thank': False})

def calorie_entry(request):
    if request.method == 'POST':
        form = CalorieEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calorie_entry')  # Redirect to the same page after submission
    else:
        form = CalorieEntryForm()

    entries = CalorieEntry.objects.all()

    return render(request, 'Meal_Tracker/index.html', {'form': form, 'entries': entries})

def calorie_Burned(weight, height, age, gender, exercise_type, duration_minutes):
    BMR_MALE = 88.362
    BMR_FEMALE = 447.593
    ACTIVITY_FACTOR = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very_active': 1.9,
    }
    # print(gender)
    if gender == 'M':
        bmr = BMR_MALE + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = BMR_FEMALE + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    calories_burned = bmr * ACTIVITY_FACTOR.get(exercise_type, 1.0) * (duration_minutes / 60.0)
    return calories_burned

def Activity_Tracker(request):
    if request.method == 'POST':
        weight = float(request.POST.get('weight'))
        height = float(request.POST.get('height'))
        age = int(request.POST.get('age'))
        exercise_type = str(request.POST.get('exercise_type'))
        duration = int(request.POST.get('duration_minutes'))
        gender = str(request.POST.get('gender'))

        bmi = calculate_bmi(weight, height)
        calories_burned = calorie_Burned(weight, height, age, gender, exercise_type, duration)

        return render(request, 'Activity_Tracker/index.html', {
            'bmi_calculated': True,
            'bmi': round(bmi, 2),
            'calories_burned': round(calories_burned, 2),
        })

    return render(request, 'Activity_Tracker/index.html')

def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return bmi

# def calculate_calories_burned(weight, height, age, activity_level):
#     api_key = '4d5a3265e8bb88415d11ed602f0aa05a'
#     api_endpoint = 'https://api.nutritionix.com/v1_1/exercise'

#     payload = {
#         'query': activity_level,
#         'gender': 'male',
#         'weight_kg': weight,
#         'height_cm': height,
#         'age': age,
#     }

#     headers = {
#         'x-app-id': api_key,
#         'x-app-key': 'b23c54ae',
#     }

#     try:
#         response = requests.post(api_endpoint, data=payload, headers=headers)
#         response.raise_for_status()
#         data = response.json()

#         calories_burned = data.get('exercises', [{}])[0].get('nf_calories', 0)

#         return calories_burned

#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching calories burned: {e}")
#         return 0