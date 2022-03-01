from django.contrib import admin

# Register your models here.

from .models import Product , Orders ,OrderUpdates

admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdates)