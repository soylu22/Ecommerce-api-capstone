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
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name