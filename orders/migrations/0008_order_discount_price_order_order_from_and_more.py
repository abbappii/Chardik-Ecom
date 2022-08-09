# Generated by Django 4.0.5 on 2022-08-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='order_from',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_fee',
            field=models.PositiveIntegerField(default=0),
        ),
    ]