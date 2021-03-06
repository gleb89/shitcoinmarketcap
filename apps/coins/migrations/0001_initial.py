# Generated by Django 3.2.1 on 2021-05-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название рынка')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Главное изображение')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL рынка')),
            ],
            options={
                'verbose_name': 'Рынок',
                'verbose_name_plural': 'Рынки',
            },
        ),
        migrations.CreateModel(
            name='Coins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=55, null=True, verbose_name='Символ  монеты')),
                ('name', models.CharField(max_length=255, verbose_name='Название монеты')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание монеты')),
                ('image', models.CharField(max_length=255, null=True, verbose_name='Изображение монеты')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField(default=0, verbose_name='Цена монеты')),
                ('market_cap', models.TextField(blank=True, null=True, verbose_name='Капитализация')),
                ('volume', models.TextField(blank=True, null=True, verbose_name='Обьемы')),
                ('price_exc', models.CharField(blank=True, max_length=255, null=True, verbose_name='Изменение % 24ч')),
                ('board_price', models.JSONField()),
                ('market_exchange', models.ManyToManyField(related_name='market_list', to='coin.Exchange', verbose_name='торгуется на рынках')),
            ],
            options={
                'verbose_name': 'Coin',
                'verbose_name_plural': 'Coins',
            },
        ),
    ]
