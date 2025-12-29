from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Order, OrderItem, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        user =User(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = '__all__'

# Category Serializer
from .models import Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# orderitem serializer
class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ["id", "product", "product_name", "quantity", "price"]

# order serializer
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user = serializers.ReadOnlyField(source= 'user.username')

    class Meta:
        model = Order
        fields = "__all__"
