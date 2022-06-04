from django.contrib import admin
from Products.models import OrderItem


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 0
    can_delete = False

    def has_add_permission(self, request, obj):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'customer']
    inlines = [OrderItemAdmin]
    fields = (
        ("status", ),
        ("customer", ),
        ("shipping_address", "billing_address"),
    )
    readonly_fields = ["customer", "shipping_address", "billing_address"]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
