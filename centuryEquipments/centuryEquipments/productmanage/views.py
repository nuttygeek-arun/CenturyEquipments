from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import ProductDetails

class ProductViewSet(viewsets.ModelViewSet):
  queryset=ProductDetails.objects.all()
  serializer_class=ProductSerializer

