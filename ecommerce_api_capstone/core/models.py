from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="products"
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    image_url = models.URLField(blank=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name
    
# Category model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

# Order 
from django.db import models
from django.contrib.auth.models import User
from .models import Product

class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete = models.CASCADE, related_name = 'orders'
    )

    total_price = models.DecimalField(
        max_digits = 10,
        decimal_places = 2,
        default = 0
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order #{self.id} by {self.user.username}"

# Order item model

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete= models.CASCADE, related_name='items'
    )

    product = models.ForeignKey(
        Product, on_delete = models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"