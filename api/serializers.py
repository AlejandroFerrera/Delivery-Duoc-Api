from rest_framework import serializers
from .models import Restaurant, Product


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'title', 'location', 'logo', 'image', 'calification']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'description', 'image']
