from home.models import Product
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Order, OrderItem
from .forms import CartAddForm
from .cart import Cart


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


class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)

        for item in cart:
            OrderItem.objects.create(
                order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
        cart.clear()
        return redirect('orders:orders-detail', order.pk)


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        return render(request, 'orders/order.html', {'order': order})
