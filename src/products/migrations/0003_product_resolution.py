# Generated by Django 3.2.9 on 2021-12-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='resolution',
            field=models.CharField(blank=True, choices=[('4K', '4K'), ('HD', 'Full HD')], max_length=10, null=True),
        ),
    ]
