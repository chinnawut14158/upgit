from rest_framework import serializers
from .models import *

class ShopSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Shop
        fields = '__all__'


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'

class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = '__all__'