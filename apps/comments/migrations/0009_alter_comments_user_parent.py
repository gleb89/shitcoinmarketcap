# Generated by Django 3.2.1 on 2021-06-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0008_alter_comments_user_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='user_parent',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Юсер комментария родителя'),
        ),
    ]
