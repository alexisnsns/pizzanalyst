# Generated by Django 4.2.3 on 2023-08-14 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_alter_comment_options_remove_comment_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]