# Generated by Django 3.2.1 on 2021-06-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0013_alter_coins_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coins',
            name='price',
            field=models.DecimalField(decimal_places=10, max_digits=10, verbose_name='Цена'),
        ),
    ]
