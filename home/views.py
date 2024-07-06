from typing import Any
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin

from . models import Product, Category
from orders.forms import CartAddForm
from utils import IsAdminUserMixin


class HomeView(View):

    def get(self, request, slug=None):
        products = Product.objects.filter(availbale=True)
        categories = Category.objects.filter(is_sub=False)

        if slug:
            category = Category.objects.get(slug=slug)
            products = products.filter(category=category)

        return render(request, 'home/home.html', {'products': products, 'categories': categories})


class ProductDetailView(IsAdminUserMixin, View):

    # def test_func(self):
    #     return self.request.user.is_authenticated and self.request.user.is_admin

    def setup(self, request, *args, **kwargs):
        self.product_instance = get_object_or_404(Product, slug=kwargs['slug'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, slug):
        product = self.product_instance
        form = CartAddForm()
        return render(request, 'home/detail.html', {'product': product, 'form': form})
