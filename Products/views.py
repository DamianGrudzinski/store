from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.

def index(request):
    available_products = Product.objects.all()
    return HttpResponse(available_products)
