# Generated by Django 4.1.1 on 2022-10-21 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='code',
            field=models.CharField(max_length=3, unique=True, verbose_name='Código'),
        ),
    ]
