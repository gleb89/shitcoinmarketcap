# Generated by Django 3.2.1 on 2021-06-06 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0010_alter_coins_market_exchange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coins',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
    ]
