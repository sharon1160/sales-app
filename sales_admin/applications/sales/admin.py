from django.contrib import admin

from applications.warehouse.models import Currency
from applications.sales.models import Customer
from applications.sales.models import Order
from applications.sales.models import OrderItem


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Clase para personalizar cómo queremos con el modelo Customer
    en Django Admin.
    """

    # Definimos los atributos que queremos que se muestren en el listado de pedidos
    list_display = ['code', 'business_name', 'district', 'category', 'ruc']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Clase para personalizar cómo queremos con el modelo Order
    en Django Admin.
    """

    # Definimos los atributos que queremos mostrar en django admin (formulario)
    fields = ('number', 'date', 'delivery_address',
              'delivery_date', 'customer_id')

    # Definimos los atributos que queremos que se muestren en el listado de pedidos
    list_display = ['number', 'date', 'delivery_address',
                    'delivery_date', 'customer_id', 'subtotal', 'igv', 'total', 'discount_total']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    Clase para personalizar cómo queremos con el modelo OrderItem
    en Django Admin.
    """

    # Definimos los atributos que queremos mostrar en django admin (formulario)
    fields = ('order_id', 'product_id', 'quantity')

    # Definimos los atributos que queremos que se muestren en el listado de detalles
    list_display = ['order_id', 'product_id',
                    'display_base_sale_price', 'display_percent_discount', 'display_sale_price', 'quantity', 'display_total']

    def display_base_sale_price(self, obj) -> str:
        """
        Método que devuelve el precio base de venta del producto con el simbolo
        de la moneda.
        """
        return f"{obj.product_id.currency_id.symbol} {obj.product_id.base_sale_price}"

    # Defimos el nombre de la columna
    display_base_sale_price.short_description = "Precio Unitario"

    def display_sale_price(self, obj) -> str:
        """
        Método que devuelve el precio de venta del producto con el simbolo
        de la moneda.
        """
        return f"{obj.product_id.currency_id.symbol} {obj.product_id.sale_price}"

    # Defimos el nombre de la columna
    display_sale_price.short_description = "Precio de Venta"

    def display_percent_discount(self, obj) -> str:
        """
          Método que devuelve el precio de venta del producto con el simbolo
          de la moneda.
        """
        return f"{obj.product_id.percent_discount}%"

    # Defimos el nombre de la columna
    display_percent_discount.short_description = "Descuento (%)"

    def display_total(self, obj) -> str:
        """
          Método que devuelve el precio de venta del producto con el simbolo
          de la moneda.
        """
        return f"{obj.product_id.currency_id.symbol} {obj.total}"

    # Defimos el nombre de la columna
    display_total.short_description = "Total"


# Agregamos al modelo Currency al django admin
admin.site.register(Currency)  # REVISAR
