# Generated by Django 4.0.5 on 2022-08-10 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_order_discount_price_order_order_from_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.PositiveIntegerField(default=0),
        ),
    ]