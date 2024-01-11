from django import forms
from .models import CalorieEntry, CaloriesBurned

class CalorieEntryForm(forms.ModelForm):
    class Meta:
        model = CalorieEntry
        fields = ['calories_consumed', 'time', 'date']
        
class CalorieBurnedEntryForm(forms.ModelForm):
    class Meta:
        model = CaloriesBurned
        fields = ['time', 'date', 'weight', 'age', 'gender', 'exercise_type', 'duration_minutes']