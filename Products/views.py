from django.views.generic import ListView, DetailView
from Products.models import *


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = context['category'].get_descendants()
        context["products"] = Product.objects.filter(category=context['category'])
        return context


class IndexView(ListView):
    model = Category


class ProductDetailView(DetailView):
    model = Product
