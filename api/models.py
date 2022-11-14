from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)


class Restaurant(models.Model):

    title = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    logo = models.URLField(blank=True)
    image = models.URLField(blank=True)
    calification = models.DecimalField(max_digits=2, decimal_places=1)
    favorite = models.ManyToManyField(
        User, related_name="favorites", blank=True)

    def __str__(self):
        return f"{self.title} - {self.location}"


class Product(models.Model):

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField(blank=True)
    description = models.CharField(max_length=170)

    def __str__(self):
        return f"{self.title}"


class ShippingCost(models.Model):
    min_distance = models.IntegerField()
    max_distance = models.IntegerField()
    cost = models.IntegerField()

    def __str__(self):
        return f"{self.min_distance}km - {self.max_distance}km -> CLP{self.cost}"


class Commission(models.Model):
    receiver = models.CharField(max_length=40)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.receiver} - {self.percentage}%"


class Order(models.Model):

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    commission = models.ForeignKey(
        Commission, on_delete=models.CASCADE, blank=True)
    shipping_cost = models.ForeignKey(ShippingCost, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order: {self.id}"


class OrderDetail(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.order} -> Producto: {self.product}, Cantidad: {self.quantity} "


class HistoricPayments(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    nro_boleta = models.IntegerField()
    products_total = models.IntegerField()
    commission_price = models.IntegerField()
    shipping_price = models.IntegerField()
    total = models.IntegerField()
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
