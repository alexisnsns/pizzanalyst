# Generated by Django 4.2.3 on 2023-08-11 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurants', '0006_alter_restaurant_options_restaurant_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'permissions': [('can_delete_comment', 'Can delete comment')]},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='username',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
