# Generated by Django 4.1.1 on 2022-10-21 01:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('warehouse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=3, unique=True, verbose_name='Código')),
                ('business_name', models.CharField(max_length=50, verbose_name='Razón Social')),
                ('district', models.CharField(max_length=60, verbose_name='Distrito')),
                ('category', models.CharField(max_length=50, verbose_name='Categoría')),
                ('ruc', models.CharField(max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(11)], verbose_name='RUC')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
            ],
            options={
                'verbose_name': 'Cliente',
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=5, unique=True, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Número de Pedido')),
                ('date', models.DateTimeField(verbose_name='Fecha de Pedido')),
                ('delivery_address', models.CharField(max_length=150, verbose_name='Dirección de Entrega')),
                ('delivery_date', models.DateTimeField(verbose_name='Fecha de Entrega')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Subtotal')),
                ('igv', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='IGV')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Total')),
                ('discount_total', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Descuento Total')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('customer_id', models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.CASCADE, to='sales.customer', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Pedido',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(200)], verbose_name='Cantidad')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Total')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('order_id', models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, to='sales.order', verbose_name='Pedido')),
                ('product_id', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='warehouse.product', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Item Pedido',
                'db_table': 'order_item',
            },
        ),
    ]
