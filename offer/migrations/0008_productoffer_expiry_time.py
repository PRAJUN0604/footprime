# Generated by Django 4.2.10 on 2024-02-07 07:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0007_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoffer',
            name='expiry_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
