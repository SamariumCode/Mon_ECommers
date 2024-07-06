from django.urls import path


from . import views


app_name = 'orders'

urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='orders-create'),
    path('detail/<int:pk>/', views.OrderDetailView.as_view(), name='orders-detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/<int:pk>/', views.CartAddView.as_view(), name='cart-add'),
    path('cart/remove/<int:pk>/', views.CartRemoveView.as_view(), name='cart-remove'),
]
