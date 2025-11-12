from django.urls import path
from .views import ContactCreateView, ProductListCreateView

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact-create'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
]
