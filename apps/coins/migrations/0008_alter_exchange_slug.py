# Generated by Django 3.2.1 on 2021-06-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0007_alter_coins_market_cap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='slug'),
        ),
    ]
