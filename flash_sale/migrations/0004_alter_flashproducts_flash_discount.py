# Generated by Django 3.2.6 on 2022-08-07 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flash_sale', '0003_remove_flashsale_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashproducts',
            name='flash_discount',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Flash Discount Percantage'),
        ),
    ]
