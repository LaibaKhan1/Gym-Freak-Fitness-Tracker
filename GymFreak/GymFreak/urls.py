"""
URL configuration for GymFreak project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='GymFreak'),
    path("Blog/", views.blog, name='Blog'),
    path("Ex_Routines/", views.Ex_Routines, name='Ex_Routines'),
    path("exercise/<int:myid>", views.exerciseView, name='exercise'),
    path("Activity_Tracker/", views.Activity_Tracker, name='Activity_Tracker'),
    path("Meal_Tracker/", views.Meal_Tracker, name='Meal_Tracker'),
    path('loginn/', views.loginn, name='loginn'),
    path('signup/', views.signup, name='signup'),
    # path('register/', your_register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
