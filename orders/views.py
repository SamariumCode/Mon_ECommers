from home.models import Product
from django.shortcuts import render, get_object_or_404, redirect


from django.views import View
from .cart import Cart
from .forms import CartAddForm


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'orders/cart.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, pk):
        cart = Cart(request)
        product = get_object_or_404(Product, pk=pk)
        form = CartAddForm(request.POST)

        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
            return redirect('orders:cart')


class CartRemoveView(View):
    def get(self, request, pk):
        cart = Cart(request)
        product = get_object_or_404(Product, pk=pk)
        cart.remove(product)
        return redirect('orders:cart')
