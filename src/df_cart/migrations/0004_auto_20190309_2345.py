# Generated by Django 2.1.7 on 2019-03-09 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_cart', '0003_auto_20190308_1639'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartinfo',
            options={'verbose_name': 'cart_product_info', 'verbose_name_plural': 'cart_product_info'},
        ),
    ]