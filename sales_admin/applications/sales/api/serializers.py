from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from applications.sales.models import Order, OrderItem, Customer


class OrderSerializer(ModelSerializer):
    """
    Clase para convertir un objeto Order a un formato JSON
    """
    business_name = SerializerMethodField('get_business_name')

    def get_business_name(self, order):
        return order.customer_id.business_name

    class Meta:
        model = Order
        fields = ['id', 'number', 'date', 'business_name',
                  'delivery_date', 'subtotal', 'igv', 'total', 'discount_total']


class OrderItemSerializer(ModelSerializer):
    """
    Clase para convertir un objeto OrderItem a un formato JSON
    """

    def validate_stock(self, data):
        quantity = data["quantity"]
        product_id = data["product_id"]
        if quantity > self.product_id.stock:
            return serializer.is_valid(raise_exception=True)
        return data

    class Meta:
        model = OrderItem
        fields = '__all__'


class CustomerSerializer(ModelSerializer):
    """
    Clase para convertir un objeto Customer a un formato JSON
    """
    class Meta:
        model = Customer
        fields = '__all__'
