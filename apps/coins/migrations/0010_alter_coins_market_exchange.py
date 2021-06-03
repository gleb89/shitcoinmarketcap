# Generated by Django 3.2.1 on 2021-06-03 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0009_alter_coins_market_exchange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coins',
            name='market_exchange',
            field=models.ManyToManyField(blank=True, related_name='market_list', to='coin.Exchange', verbose_name='торгуется на рынках'),
        ),
    ]
