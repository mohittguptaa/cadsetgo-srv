from rest_framework import generics
from .models import Contact, Product
from .serializers import ContactSerializer, ProductSerializer

class ContactCreateView(generics.CreateAPIView):
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer

class ProductListCreateView(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
