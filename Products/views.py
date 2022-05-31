from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from Products.models import Product, Category


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["products"] = Product.objects.filter(category=context['category'])
        return context


class ProductListView(ListView):
    # model = Product
    model = Category
