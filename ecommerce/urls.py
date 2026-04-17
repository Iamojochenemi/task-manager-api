from django.urls import path
from .views import ProductListCreateView, ProductDetailView, OrderListView, RegisterView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('register/', RegisterView.as_view(), name='register'),
]
