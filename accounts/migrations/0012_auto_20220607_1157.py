# Generated by Django 3.2.6 on 2022-06-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
