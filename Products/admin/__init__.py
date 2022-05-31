from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .product import ProductAdmin
from ..models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Club)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
