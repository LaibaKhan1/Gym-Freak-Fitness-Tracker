from django import forms
from .models import CalorieEntry, CaloriesBurnedEntry, CustomUser
from django.contrib.auth.forms import UserCreationForm
class CalorieEntryForm(forms.ModelForm):
    class Meta:
        model = CalorieEntry
        fields = ['calories_consumed', 'time', 'date']
        
class CaloriesBurnedEntryForm(forms.ModelForm):
    class Meta:
        model = CaloriesBurnedEntry
        fields = ['calories_burned', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
        
class CustomUserCreationForm(UserCreationForm):
    profile_pic = forms.ImageField(required=False)
    email = forms.CharField(max_length=50, required=False)
    contact_number = forms.CharField(max_length=11, required=False)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'contact_number', 'profile_pic')