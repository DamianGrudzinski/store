from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    fields = (
        ('name', ),
        ('category', ),
        ('price', ),
        ('description', ),
    )
