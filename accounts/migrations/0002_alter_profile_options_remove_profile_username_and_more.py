# Generated by Django 4.0.4 on 2022-05-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'Profile'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=300, null=True, unique=True, verbose_name='Username'),
        ),
    ]