# Generated by Django 3.2.15 on 2022-12-03 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20221130_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='', upload_to='uploads/'),
        ),
    ]
