# Generated by Django 3.2.6 on 2022-06-17 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20220618_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='expire_rate',
            field=models.DateField(blank=True, null=True),
        ),
    ]