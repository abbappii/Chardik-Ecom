# Generated by Django 4.0.4 on 2022-06-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_merge_20220629_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
