# Generated by Django 4.0.5 on 2022-07-23 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_name_outlet_expenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='expence_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
    ]
