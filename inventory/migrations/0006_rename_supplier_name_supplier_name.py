# Generated by Django 4.0.5 on 2022-08-11 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_rename_name_supplier_supplier_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='supplier_name',
            new_name='name',
        ),
    ]
