from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from Products.models import *


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = context['category'].get_descendants()
        context["products"] = Product.objects.filter(category=context['category'])
        return context


class ProductDetailView(DetailView):
    model = Product

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        if request.user.is_authenticated:
            cart, _ = Cart.objects.get_or_create(customer=request.user)
            cart_item, _ = CartItem.objects.get_or_create(cart=cart, product=self.object, defaults={'quantity': 0})
            cart_item.quantity += 1
            cart_item.save()

        return redirect('product', self.object.id)


class IndexView(ListView):
    model = Category
    template_name = "Products/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["new_products"] = Product.objects.order_by('-id').all()[:4]
        return context


class CartView(LoginRequiredMixin, TemplateView):
    model = Cart
    template_name = 'Products/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            cart, _ = Cart.objects.get_or_create(customer=self.request.user)
            context["cart"] = cart

        return context

    def post(self, request, *args, **kwargs):
        if "item_id" in request.POST:
            try:
                CartItem.objects.get(
                    id=request.POST["item_id"],
                    cart__customer=request.user,
                ).delete()
            except CartItem.DoesNotExist:
                pass

        return redirect('cart')


class OrderView(LoginRequiredMixin, TemplateView):
    template_name = 'Products/order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart, _ = Cart.objects.get_or_create(customer=self.request.user)
        context["cart"] = cart

        return context

    def post(self, request, *args, **kwargs):
        try:
            cart = Cart.objects.get(customer=self.request.user)
        except Cart.DoesNotExist:
            cart = None

        if cart and cart.items.count() and "place_order" in request.POST:
            order = Order.objects.create(
                customer=self.request.user,
                billing_address=request.POST["billing_address"],
                shipping_address=request.POST["shipping_address"],
            )

            for cart_item in cart.items.all():
                order_item = OrderItem.objects.create(
                    product=cart_item.product,
                    order=order,
                    price=cart_item.product.price,
                    quantity=cart_item.quantity,
                    total_price=cart_item.product.price*cart_item.quantity,
                )
                order_item.save()
                cart_item.delete()
            return redirect('user_orders')

        return redirect('cart')


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'Products/user_profile.html'


class UserOrdersView(LoginRequiredMixin, TemplateView):
    template_name = 'Products/user_orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = Order.objects.filter(customer=self.request.user).annotate(
            order_total=Coalesce(Sum('items__total_price'), Value(Decimal('0')))
        ).all().order_by('-created_at')
        return context
