# Generated by Django 4.0.5 on 2022-07-06 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_options_alter_profile_points_gained'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='points_gained',
            field=models.IntegerField(default=0),
        ),
    ]
