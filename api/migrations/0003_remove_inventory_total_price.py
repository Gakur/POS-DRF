# Generated by Django 4.1.7 on 2023-04-10 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_inventory_total_price_alter_sales_item_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='total_price',
        ),
    ]
