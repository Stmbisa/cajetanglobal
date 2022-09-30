# Generated by Django 3.2.15 on 2022-09-30 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220930_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='brought_by',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country_of_orgin',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nationality',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='next_of_kin_phone',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
