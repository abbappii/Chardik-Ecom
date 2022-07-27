# Generated by Django 4.0.5 on 2022-07-26 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_products_is_in_flash_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='regular_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='products',
            name='reseller_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='products',
            name='selling_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='products',
            name='sold_count',
            field=models.IntegerField(default=0),
        ),
    ]