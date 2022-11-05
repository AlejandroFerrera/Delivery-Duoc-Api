from django.contrib import admin
from .models import Product, Restaurant, User, Commission, ShippingCost, Order, OrderDetail

# Register your models here.

admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Product)
admin.site.register(Commission)
admin.site.register(ShippingCost)
admin.site.register(Order)
admin.site.register(OrderDetail)

