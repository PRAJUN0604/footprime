# Generated by Django 5.0 on 2023-12-28 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
