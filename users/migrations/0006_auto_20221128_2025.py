# Generated by Django 3.2.15 on 2022-11-28 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20221128_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='has_done_biometry_before',
        ),
        migrations.RemoveField(
            model_name='user',
            name='has_paid',
        ),
    ]
