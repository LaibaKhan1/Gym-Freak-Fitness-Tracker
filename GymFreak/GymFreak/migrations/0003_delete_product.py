# Generated by Django 5.0 on 2024-01-06 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GymFreak', '0002_product_delete_orders_delete_orderupdate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
