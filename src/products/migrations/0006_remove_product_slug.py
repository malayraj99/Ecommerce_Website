# Generated by Django 3.1.3 on 2020-12-02 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
