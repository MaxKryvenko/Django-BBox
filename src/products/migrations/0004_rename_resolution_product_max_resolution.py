# Generated by Django 3.2.9 on 2021-12-07 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_resolution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='resolution',
            new_name='max_resolution',
        ),
    ]
