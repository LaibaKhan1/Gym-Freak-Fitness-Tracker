from django import forms
from .models import CalorieEntry

class CalorieEntryForm(forms.ModelForm):
    class Meta:
        model = CalorieEntry
        fields = ['calories_consumed', 'time', 'date']