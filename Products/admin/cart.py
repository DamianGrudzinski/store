from django.contrib import admin
from Products.models import CartItem


class CartItemAdmin(admin.TabularInline):
    model = CartItem
    extra = 0


class CartAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'customer']
    inlines = [CartItemAdmin]
