"""
En el archivo models.py agregamos los modelos que utilizará nuestra aplicación.
Los modelos de esta aplicación pueden ser utilizados desde otras aplicaciones.
"""
# Importamos la clase MinLengthValidator para agregar validacion
# Link: https://docs.djangoproject.com/en/4.1/ref/validators/#module-django.core.validators
from django.core.validators import MinLengthValidator

# Importamos las clases MinValueValidator, MaxValueValidator para agregar validaciones
# al atributo "quantity"
# Link: https://docs.djangoproject.com/en/4.1/ref/validators/#module-django.core.validators
from django.core.validators import MinValueValidator, MaxValueValidator

# Importamos la clase models del módulo django.db
# Link: https://docs.djangoproject.com/en/4.1/topics/db/models/
from django.db import models

# Importamos la clase Product de la aplicación Warehouse
from applications.warehouse.models import Product


class Customer(models.Model):
    """
    Clase Cliente

    """
    id = models.AutoField(primary_key=True)

    code = models.CharField(max_length=3, unique=True, verbose_name="Código")

    # razon social
    business_name = models.CharField(
        max_length=50, blank=False, verbose_name="Razón Social")

    # distrito
    district = models.CharField(
        max_length=60, verbose_name="Distrito")

    # categoria
    category = models.CharField(max_length=50, verbose_name="Categoría")

    # RUC del cliente (único, y de 11 dígitos)
    ruc = models.CharField(unique=True, max_length=11, validators=[
        MinLengthValidator(11)], verbose_name="RUC")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        db_table = "customer"
        verbose_name = "Cliente"


class Order(models.Model):
    """
    Clase Pedido

    """
    id = models.AutoField(primary_key=True)

    # numero de pedido
    number = models.CharField(unique=True, max_length=5, validators=[
                              MinLengthValidator(5)], verbose_name="Número de Pedido")

    # fecha de pedido
    date = models.DateTimeField(verbose_name="Fecha de Pedido")

    # direccion de entrega
    delivery_address = models.CharField(
        max_length=150, verbose_name="Dirección de Entrega")

    # fecha de entrega
    delivery_date = models.DateTimeField(verbose_name="Fecha de Entrega")

    # foreign_key: cliente
    customer_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, db_column="customer_id", verbose_name="Cliente")

    subtotal = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Subtotal")

    igv = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="IGV")

    total = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Total")

    # descuento total
    discount_total = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Descuento Total")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        db_table = "order"
        verbose_name = "Pedido"


class OrderItem(models.Model):
    """
    Clase Item del pedido

    """
    id = models.AutoField(primary_key=True)

    # foreign_key: Pedido
    order_id = models.ForeignKey(
        Order, on_delete=models.CASCADE, db_column="order_id", verbose_name="Pedido")

    # foreign_key: Producto
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column="product_id", verbose_name="Producto")

    # cantidad de productos
    quantity = models.PositiveSmallIntegerField(default=0, validators=[
        MinValueValidator(0), MaxValueValidator(200)], verbose_name="Cantidad")

    total = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, verbose_name="Total")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de Modificación")

    class Meta:
        db_table = "order_item"
        verbose_name = "Item Pedido"
