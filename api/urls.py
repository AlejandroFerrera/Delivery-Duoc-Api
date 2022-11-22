from django.urls import path
from api import views

urlpatterns = [
    path('', views.end_points),
    path('api/restaurants/', views.get_restaurants),
    path('api/restaurants/<str:id>', views.get_restaurant),
    path('api/restaurants/<str:id>/products', views.get_products),
    path('api/product/<str:id>', views.get_product),
    path('api/order', views.create_order),
    path('api/random_shipping_price', views.get_random_shipping_price),
    path('api/login', views.login),
    path('api/create_user', views.create_user)
]
