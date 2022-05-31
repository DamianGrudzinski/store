from django.contrib import admin
from mptt.admin import MPTTModelAdmin


class ProductAdmin(admin.ModelAdmin):
    fields = (
        ('name', ),
        ('category', 'club', ),
        ('price', ),
        ('description', ),
    )