# Generated by Django 3.2.6 on 2022-08-05 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revenue', '0002_alter_revenuehistory_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenuehistory',
            name='profits',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
