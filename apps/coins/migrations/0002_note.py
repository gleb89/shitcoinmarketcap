# Generated by Django 3.2.1 on 2021-05-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
    ]
