from rest_framework import serializers
from .models import ProductDetails

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=ProductDetails
        fields='__all__'