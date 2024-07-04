from django.urls import path

from . import views


app_name = 'home'

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('category/<slug:slug>/', views.HomeView.as_view(),
         name='category-filter'),
    path('category/<slug:slug>/', views.ProductDetailView.as_view(),
         name='product-detail'),

]
