from django import forms
from .models import CalorieEntry, CaloriesBurned, CustomUser
from django.contrib.auth.forms import UserCreationForm
class CalorieEntryForm(forms.ModelForm):
    class Meta:
        model = CalorieEntry
        fields = ['calories_consumed', 'time', 'date']
        
class CalorieBurnedEntryForm(forms.ModelForm):
    class Meta:
        model = CaloriesBurned
        fields = ['time', 'date', 'weight', 'age', 'gender', 'exercise_type', 'duration_minutes']
        
class CustomUserCreationForm(UserCreationForm):
    profile_pic = forms.ImageField(required=False)
    email = forms.CharField(max_length=50, required=False)
    contact_number = forms.CharField(max_length=11, required=False)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'contact_number', 'profile_pic')