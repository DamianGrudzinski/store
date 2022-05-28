from django.contrib import admin

from .models import Product, Club, Category

# Register your models here.

admin.site.register(Product)
admin.site.register(Club)
admin.site.register(Category)
