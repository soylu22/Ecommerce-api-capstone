from django.contrib import admin

from core import permissions
from core.serializers import OrderSerializer
from rest_framework import generics, permissions

# Register your models here.
from .models import Order, Product

admin.site.register(Product)

class AdminOrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]