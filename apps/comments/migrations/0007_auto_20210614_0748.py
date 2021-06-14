# Generated by Django 3.2.1 on 2021-06-14 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0006_comments_user_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.AddField(
            model_name='comments',
            name='user_id',
            field=models.CharField(default=1, max_length=255, verbose_name='Юсер комментария'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='user_parent',
            field=models.CharField(default=1, max_length=255, verbose_name='Юсер комментария родителя'),
            preserve_default=False,
        ),
    ]
