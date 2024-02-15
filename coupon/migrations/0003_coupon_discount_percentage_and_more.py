# Generated by Django 5.0 on 2024-01-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0002_rename_discount_percentage_coupon_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='discount_percentage',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount_price',
            field=models.FloatField(default=0),
        ),
    ]
