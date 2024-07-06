from django.urls import path


from . import views


app_name = 'orders'

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/<int:pk>/', views.CartAddView.as_view(), name='cart-add'),
    path('cart/remove/<int:pk>/', views.CartRemoveView.as_view(), name='cart-remove'),
]
