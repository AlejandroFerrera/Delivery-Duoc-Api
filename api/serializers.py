from rest_framework import serializers
from .models import Restaurant, Product, Order, OrderDetail


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'title', 'location', 'logo', 'image', 'calification']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','restaurant_id', 'title', 'price', 'description', 'image']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderDetailSerializer(serializers.Serializer):
    
    order_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `OrderDetail` instance, given the validated data.
        """

        return OrderDetail.objects.create(**validated_data)