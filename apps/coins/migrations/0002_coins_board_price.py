# Generated by Django 3.2.1 on 2021-05-11 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coins',
            name='board_price',
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
    ]
