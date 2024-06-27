# products/urls.py

from django.urls import path
from .views import MyTokenObtainPairView, ProductListCreateView, ProductDetailView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
