# Generated by Django 4.2.3 on 2023-08-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0011_alter_restaurant_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='address_search',
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='address',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]