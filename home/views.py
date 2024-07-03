from typing import Any
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views import View

from . models import Product


class HomeView(View):

    def get(self, request):
        products = Product.objects.filter(availbale=True)
        return render(request, 'home/home.html', {'products': products})


class ProductDetailView(View):

    def setup(self, request, *args, **kwargs):
        self.product_instance = get_object_or_404(Product, slug=kwargs['slug'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, slug):
        product = self.product_instance
        return render(request, 'home/detail.html', {'product': product})
