from django.contrib import admin

from .models import Ex_Routines, Orders, OrderUpdate

# Register your models here.
admin.site.register(Ex_Routines)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
