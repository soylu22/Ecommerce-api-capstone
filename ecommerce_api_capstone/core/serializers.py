from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Order, OrderItem, Product, Category

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
    # owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = [
            "id", "name", "description", "price", "stock_quantity",
            "category", "category_name", "image_url", "created_at"
        ]

    def validate_name(self, value):
        if not value or value.strip() == "":
            raise serializers.ValidationError("Product name is required.")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value

    def validate_stock_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative.")
        return value

# Category Serializer
from .models import Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# orderitem serializer
class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)
    # product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ["product", "product_name", "quantity", "price"]

# order serializer
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, write_only=True)
    # user = serializers.ReadOnlyField(source= 'user.username')

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ['total_price', 'created_at']
