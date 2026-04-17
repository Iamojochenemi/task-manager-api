from rest_framework import serializers
from .models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True) 
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'product_name', 'product_price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, )
    total_price = serializers.SerializerMethodField()
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'total_price', 'items', 'created_at', 'status']

    def get_total_price(self, obj):
        total = sum(item.product.price * item.quantity for item in obj.items.all())
        return total
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order
    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("Order must contain at least one item.")
        return value
    