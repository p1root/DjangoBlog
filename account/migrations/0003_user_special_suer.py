# Generated by Django 4.2.3 on 2023-08-15 07:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='special_suer',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]