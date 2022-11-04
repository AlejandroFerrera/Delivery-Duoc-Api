from django.contrib import admin
from .models import Product, Restaurant, User

# Register your models here.

admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Product)

