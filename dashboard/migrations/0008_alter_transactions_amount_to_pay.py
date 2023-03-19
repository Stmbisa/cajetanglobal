# Generated by Django 3.2.15 on 2023-03-19 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_transactions_amount_to_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='amount_to_pay',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=15, max_length=255, null=True),
        ),
    ]
