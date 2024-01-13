from django.db import models
from django.contrib.auth.models import AbstractUser
    
class ex_routines(models.Model):
    routine_id = models.AutoField
    routine_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=1000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='Ex_Routines/images', default="")
    step1_image = models.ImageField(upload_to='Ex_Routines/step1', default="")
    step2_image = models.ImageField(upload_to='Ex_Routines/step2', default="")
    step3_image = models.ImageField(upload_to='Ex_Routines/step3', default="")
    step4_image = models.ImageField(upload_to='Ex_Routines/step4', default="")
    step5_image = models.ImageField(upload_to='Ex_Routines/step5', default="")
    step6_image = models.ImageField(upload_to='Ex_Routines/step6', default="")

    def __str__(self):
        return self.routine_name
    
class CalorieEntry(models.Model):
    calories_consumed = models.FloatField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.calories_consumed} calories on {self.date} at {self.time}'
    
class BMIEntry(models.Model):
    bmi_value = models.FloatField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'BMI: {self.bmi_value} on {self.date} at {self.time}'
    
class CaloriesBurnedEntry(models.Model):
    calories_burned = models.FloatField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'Calories Burned: {self.calories_burned} on {self.date} at {self.time}'
    
class LoginPageSettings(models.Model):
    background_image = models.ImageField(upload_to='loginPage/')
    
class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    contact_number = models.CharField(max_length=11, null=True, blank=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        related_query_name='user',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        related_query_name='user',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )