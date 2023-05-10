from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Customer,Product
from .serializers import CustomerSerializer,ProductSerializer
from django.utils import timezone
from datetime import timedelta

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        product = serializer.save()
        if not product.is_active:
            two_months = timezone.now() - timedelta(days=60)
            
            if product.registered_at <= two_months:
                product.is_active = False
                product.save()    