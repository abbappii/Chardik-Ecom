# Generated by Django 4.0.5 on 2022-07-23 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_expire_rate_products_expire_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='quantity',
        ),
        migrations.AddField(
            model_name='products',
            name='attribute',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
