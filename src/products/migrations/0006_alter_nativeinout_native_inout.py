# Generated by Django 3.2.9 on 2021-12-08 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20211208_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nativeinout',
            name='native_inout',
            field=models.CharField(choices=[('VGA', 'VGA'), ('DVI', 'DVI'), ('HDMI', 'HDMI'), ('DP', 'DsiplayPort')], max_length=10),
        ),
    ]
