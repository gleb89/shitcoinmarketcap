# Generated by Django 3.2.1 on 2021-05-25 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0003_auto_20210525_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchange',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='slug'),
        ),
    ]
