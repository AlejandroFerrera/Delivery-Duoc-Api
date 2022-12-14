from django.shortcuts import render
from .serializers import RestaurantSerializer, ProductSerializer, OrderDetailSerializer
from .models import Restaurant, Product, OrderDetail, Order, User, Commission, ShippingCost
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
import random


@api_view(['GET'])
def end_points(request):

    end_points = {
        'All restaurants': 'GET api/restuarants'
    }

    return Response(end_points)


@api_view(['GET'])
def get_random_shipping_price(request):
    if request.method == 'GET':
        random_id = random.randint(1, ShippingCost.objects.count())
        price = ShippingCost.objects.get(id=random_id).cost
        return Response({'id': random_id, 'price': price})


@api_view(['GET'])
def get_restaurants(request):
    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_restaurant(request, id):
    if request.method == 'GET':
        restaurant = Restaurant.objects.get(id=id)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)


@api_view(['GET'])
def get_products(request, id):

    if request.method == 'GET':
        restaurant = Restaurant.objects.get(id=id)
        products = Product.objects.filter(restaurant=restaurant)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_product(request, id):

    if request.method == 'GET':
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def create_order(request):

    # Random Shipping Cost
    random_shipping_id = random.randint(1, ShippingCost.objects.count())

    new_order = Order(client=User.objects.last(), status='pagada',
                      commission=Commission.objects.last(), shipping_cost=ShippingCost.objects.get(id=random_shipping_id))

    details = JSONParser().parse(request)
    new_order.save()

    for detail in details:
        product = Product.objects.get(id=detail['id'])
        product_quantity = detail['quantity']

        new_order_detail = OrderDetail(
            order=new_order, product=product, quantity=product_quantity)

        new_order_detail.save()

    new_order.save()

    return Response("Orden confirmada")


@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    username = data['email']
    password = data['password']

    try:
        user = User.objects.get(email=username)
    except:
        return Response('Usuario invalido')

    pass_valido = check_password(password, user.password)

    if not pass_valido:
        return Response("Password incorrecta")

    token, created = Token.objects.get_or_create(user=user)
    return Response({"id": user.id, "token": token.key})

@api_view(['POST'])
def create_user(request):

    data = JSONParser().parse(request)

    username = data['email']
    password = data['password']

    new_user = User.objects.create()

    new_user.email = username
    new_user.username = username
    new_user.set_password(password)

    new_user.save()

    return Response(new_user)