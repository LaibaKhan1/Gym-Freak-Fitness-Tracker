from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import ex_routines, CustomUser
from .models import ex_routines

# Register your models here.
admin.site.register(ex_routines)
# admin.site.register(CustomUser, UserAdmin)
# admin.site.register(Product)
# admin.site.register(Orders)
# admin.site.register(OrderUpdate)
