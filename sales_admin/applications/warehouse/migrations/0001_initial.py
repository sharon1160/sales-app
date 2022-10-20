# Generated by Django 4.1.1 on 2022-10-20 22:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=3, unique=True, verbose_name='Código')),
                ('symbol', models.CharField(max_length=4, verbose_name='Simbolo')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
            ],
            options={
                'verbose_name': 'Moneda',
                'db_table': 'currency',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=3, unique=True, verbose_name='Código')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('percent_discount', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)], verbose_name='Descuento (%)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de Mo')),
            ],
            options={
                'verbose_name': 'Categoría de Producto',
                'db_table': 'product_category',
            },
        ),
        migrations.CreateModel(
            name='UnitMeasureCategory',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=3, unique=True, verbose_name='Código')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de Mo')),
            ],
            options={
                'verbose_name': 'Categoría de Unidades de Medida',
                'db_table': 'unit_measure_category',
            },
        ),
        migrations.CreateModel(
            name='UnitMeasure',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=3, unique=True, verbose_name='Código')),
                ('name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de Mo')),
                ('unit_measure_category_id', models.ForeignKey(db_column='unit_measure_category_id', default=None, on_delete=django.db.models.deletion.CASCADE, to='warehouse.unitmeasurecategory', verbose_name='Categoría de Unidad de Medida')),
            ],
            options={
                'verbose_name': 'Unidades de Medida',
                'db_table': 'unit_measure',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=5, unique=True, verbose_name='Código')),
                ('name', models.CharField(default=None, max_length=60, verbose_name='Nombre')),
                ('purchase_price', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Precio de Compra')),
                ('base_sale_price', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Precio de Venta Base')),
                ('percent_discount', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)], verbose_name='Descuento (%)')),
                ('discount_amount', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Monto Descuento')),
                ('sale_price', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='Precio de Venta')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Stock')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')),
                ('currency_id', models.ForeignKey(db_column='currency_id', default=None, on_delete=django.db.models.deletion.CASCADE, to='warehouse.currency', verbose_name='Moneda')),
                ('product_category_id', models.ForeignKey(db_column='product_category_id', default=None, on_delete=django.db.models.deletion.CASCADE, to='warehouse.productcategory', verbose_name='Categoría Producto')),
                ('unit_measure_id', models.ForeignKey(db_column='unit_measure_id', default=None, on_delete=django.db.models.deletion.CASCADE, to='warehouse.unitmeasure', verbose_name='Unidad de Medida')),
            ],
            options={
                'verbose_name': 'Producto',
                'db_table': 'product',
            },
        ),
    ]
