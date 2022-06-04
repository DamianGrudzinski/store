from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .cart import CartAdmin
from .order import OrderAdmin
from .product import ProductAdmin
from ..models import *

admin.site.register(Cart, CartAdmin)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
