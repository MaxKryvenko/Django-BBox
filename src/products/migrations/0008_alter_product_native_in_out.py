# Generated by Django 3.2.9 on 2021-12-08 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20211208_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='native_in_out',
            field=models.ManyToManyField(blank=True, to='products.NativeInOut'),
        ),
    ]