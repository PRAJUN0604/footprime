# Generated by Django 5.0.1 on 2024-02-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0017_remove_product_offer'),
        ('offer', '0004_remove_offer_discount_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryoffer',
            name='discount_percentage',
        ),
        migrations.AddField(
            model_name='categoryoffer',
            name='discount_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='productoffer',
            name='discount_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.DeleteModel(
            name='Offer',
        ),
    ]
