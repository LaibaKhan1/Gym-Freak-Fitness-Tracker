from django.contrib import admin

from .models import ex_routines, Orders, OrderUpdate

# Register your models here.
admin.site.register(ex_routines)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
