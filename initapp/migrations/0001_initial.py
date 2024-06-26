# Generated by Django 4.0.5 on 2022-07-31 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('personName', models.CharField(max_length=300, null=True, verbose_name='Person Name')),
                ('subject', models.CharField(max_length=400, null=True, verbose_name='Subject')),
                ('c_message', models.TextField(blank=True, null=True)),
                ('email', models.CharField(max_length=300, null=True, verbose_name='Email')),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
    ]
