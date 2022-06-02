from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .product import ProductAdmin
from ..models import *

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Product, ProductAdmin)

