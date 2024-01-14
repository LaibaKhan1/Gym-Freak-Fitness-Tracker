from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ex_routines, LoginPageSettings

admin.site.register(ex_routines)
admin.site.register(LoginPageSettings)

