# Generated by Django 4.0.5 on 2022-09-08 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_products_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='title',
            field=models.CharField(max_length=180, null=True, verbose_name='Banner Title'),
        ),
    ]