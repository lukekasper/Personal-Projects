# Generated by Django 3.2.15 on 2022-12-16 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0017_rename_likes_user_liked_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]