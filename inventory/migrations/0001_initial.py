# Generated by Django 3.2.7 on 2022-07-26 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('bank_name', models.CharField(max_length=255, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
            ],
            options={
                'verbose_name_plural': 'BankAccounts',
            },
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Names',
            },
        ),
        migrations.CreateModel(
            name='Outlet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Outlets',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='Supplier Name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('address', models.TextField(null=True, verbose_name='Address')),
                ('country', models.CharField(blank=True, max_length=200, null=True, verbose_name='Country Name')),
            ],
            options={
                'verbose_name_plural': 'Supplier List',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('ref_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='Reference Number')),
                ('batch_no', models.CharField(blank=True, max_length=100, null=True, verbose_name='Batch No')),
                ('date_of_purchase', models.DateField(blank=True, null=True, verbose_name='Date of Purchase')),
                ('order_status', models.CharField(choices=[('Received', 'Recieved'), ('Pending', 'Pending'), ('Ordered', 'Ordered')], max_length=100, null=True, verbose_name='Order Status')),
                ('price', models.FloatField(null=True, verbose_name='Prce')),
                ('unit_cost', models.FloatField(blank=True, null=True, verbose_name='Net Unit Cost')),
                ('other_cost', models.FloatField(null=True, verbose_name='Other Cost')),
                ('due_price', models.FloatField(blank=True, null=True, verbose_name='Due Price')),
                ('payment_status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Partial', 'Partial'), ('Paid', 'Paid')], max_length=100, null=True, verbose_name='Payment Status')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('outlet_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_outlet_name', to='inventory.outlet')),
                ('payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bank_acc_name', to='inventory.bankaccounts')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase_product', to='products.products', verbose_name='Select product')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase', to='inventory.supplier', verbose_name='Select Supplier')),
            ],
            options={
                'verbose_name_plural': 'Purchase History',
            },
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('reference', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.CharField(blank=True, max_length=255, null=True)),
                ('expence_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('type', models.CharField(choices=[('One Time', 'One Time'), ('Repeated', 'Repeated')], max_length=200)),
                ('description', models.TextField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Bank_account', to='inventory.bankaccounts')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Expence_name', to='inventory.name')),
                ('outlet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outlet_name', to='inventory.outlet')),
            ],
            options={
                'verbose_name_plural': 'Expences',
            },
        ),
        migrations.CreateModel(
            name='DepositWithdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('Reference', models.CharField(blank=True, max_length=255, null=True)),
                ('created_by', models.CharField(blank=True, max_length=255, null=True)),
                ('transfer_type', models.CharField(choices=[('Deposit', 'Deposit'), ('Withdraw', 'Withdraw')], max_length=200)),
                ('note', models.TextField(blank=True, max_length=1000)),
                ('date_field', models.CharField(blank=True, max_length=255, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='inventory.bankaccounts', verbose_name='Bank Account')),
            ],
            options={
                'verbose_name_plural': 'Deposit Withdraws',
            },
        ),
    ]
